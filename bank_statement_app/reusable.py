import json
import os

# Global variable to cache the JSON data
cached_data = None

# Functions to merge transections to single list

def merge(data):
    all_transactions = []
    for month_data in data: 
        month_transactions = month_data.get('transactions', [])
        all_transactions.extend(month_transactions)
    return all_transactions
    
def mergeTransections():
    if cached_data:
        mergedTransections = merge(data)
        return mergedTransections
    else:
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
                # Specifying the path to the JSON file
            json_file_path = os.path.join(base_dir, 'bank_statement_data.json')
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                mergedTransections = merge(data)
                return mergedTransections
            
        except FileNotFoundError:
            raise FileNotFoundError("Error, the file you requested wasn't found")
        except Exception as e:
            raise Exception("Error in reading json file")
        