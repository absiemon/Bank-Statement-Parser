from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import os
from datetime import datetime
from .reusable import cached_data, mergeTransections


# API to get all the transections
class BankStatementList(APIView):
    def get(self, request):
        global cached_data
        # Checking if data is already cached
        if cached_data:
            # Getting pagination parameters from the query string
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 10))

            # Calculating the start and end indices for pagination
            start_index = (page - 1) * page_size
            end_index = start_index + page_size

            paginated_data = cached_data[start_index:end_index]
            return Response(paginated_data)
        
        # Specifying the path to your JSON file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(base_dir, 'bank_statement_data.json')

        try:
            # Loading JSON data from the file
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
            # Caching the data for subsequent requests
            cached_data = data
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 10))

            # Calculating the start and end indices for pagination
            start_index = (page - 1) * page_size
            end_index = start_index + page_size
            paginated_data = data[start_index:end_index]
            
            return Response(paginated_data)
        except FileNotFoundError:
            return Response({'error': 'File not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': 'An error occurred while loading JSON data'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# API to get the transections within  a specific range
class TransactionSearch(APIView):
    def get(self, request):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        # Checking if both start_date and end_date are provided
        if not start_date or not end_date:
            return Response({'error': 'Both start_date and end_date parameters are required.'}, status=400)

        # Parsing the start_date and end_date as datetime objects
        try:
            start_date = datetime.strptime(start_date, '%m/%d/%Y')
            end_date = datetime.strptime(end_date, '%m/%d/%Y')
            
            if start_date > end_date:
                return Response({'error': 'Invalid date'}, status=400)
        except ValueError:
            return Response({'error': 'Invalid date format. Use MM/DD/YYYY.'}, status=400)

        try:
            # Getting all the merged transactions
            all_transactions = mergeTransections()
        except Exception as e:
            return Response({'error': 'An error occurred while getting transaction'}, status=500)
        
        # Filtering transetions from start_date to  end_date
        filtered_transactions = [transaction for transaction in all_transactions if
                    start_date <= datetime.strptime(transaction['date'], '%m/%d/%Y') <= end_date]

        return Response({'transactions': filtered_transactions})    
            
            
# API to get the Total banalce for a specific date
class GetTransactionByDate(APIView):
    def get(self, request):
        target_date = request.query_params.get('target_date', None)

        # Check if the target_date parameter is provided
        if not target_date:
            return Response({'error': 'The target_date parameter is required.'}, status=400)

        # Parse the target_date as a datetime object
        try:
            target_date = datetime.strptime(target_date, '%m/%d/%Y')
        except ValueError:
            return Response({'error': 'Invalid date format. Use MM/DD/YYYY.'}, status=400)

        try:
            # Getting all the merged transactions
            all_transactions = mergeTransections()
        except Exception as e:
            return Response({'error': 'An error occurred while getting transaction'}, status=500)
        
        # Search for the transaction matching the target date
        found_transaction = None
        for transaction in all_transactions:
            transaction_date = datetime.strptime(transaction['date'], '%m/%d/%Y')
            if transaction_date == target_date:
                found_transaction = transaction
                break

        if found_transaction:
            return Response({'transaction': found_transaction})
        else:
            return Response({'transaction': []})          
            
            
            