import pdfplumber
import re
import json
import os
from datetime import datetime

def parse_bank_statement(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        transactions = []
        current_month = None
        transaction_headers = None
        total_credit_amount = None
        total_debit_amount = None
        closing_balance = None

        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            for index, line in enumerate(lines):
                if "Period Covered:" in line:
                    statement_date = lines[index+1].split()[0]
                    date_obj = datetime.strptime(statement_date, "%m/%d/%Y")

                    # Format the datetime object to "Month Year" format
                    formatted_date = date_obj.strftime("%b %Y")
                    current_month = formatted_date
                    transactions = []
                elif "Date Description Credit Debit Balance" in line:
                    transaction_headers = line.split()
                elif "Total Credit Amount" in line:
                    total_credit_amount = line.split(':')[1].strip()
                elif "Total Debit Amount" in line:
                    total_debit_amount = line.split(':')[1].strip()
                elif "Closing Balance" in line:
                    closing_balance  = line.split(':')[1].strip()
                elif transaction_headers:
                    values = line.split()
                    start_elements = values[:1]
                    end_elements = values[-3:]
                    middle_elements = values[1:-3]

                    # Merge the middle elements into a single string
                    merged_middle = ' '.join(middle_elements)
                    # Combine all parts into a final list
                    newValues = start_elements + [merged_middle] + end_elements
                    if len(newValues) >= len(transaction_headers) and newValues[0] !='---':
                        transaction = {key.lower(): value for key, value in zip(transaction_headers, newValues)}
                        transactions.append(transaction)
                    
            if current_month and transactions:
                #getting opening balance of current_month
                opening_balance = float(transactions[0]["balance"].replace(",", ""))
                #creating object for transection detail of a particular month (see the bank_statement_data.json for clarity)
                data_entry = {
                    "month": current_month,
                    "transactions": transactions,
                    "opening balance": str(opening_balance),
                    "total credit amount": str(total_credit_amount),
                    "total debit amount": str(total_debit_amount),
                    "closing balance": str(closing_balance),
                }
                transactions = []  # Reset transactions
                current_month = None
                yield data_entry
                
def save_json_to_file(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)
        
def main(pdf_directory, output_file):
    data = []
    # Save the JSON data to a file
    save_json_to_file(data, output_file)
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            data.extend(parse_bank_statement(pdf_path))

    # Save the JSON data to a file
    save_json_to_file(data, output_file)
    print(f"JSON data has been saved to {output_file}")

if __name__ == "__main__":
    pdf_directory = "../pdfs"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(base_dir, '../bank_statement_data.json')
    main(pdf_directory, output_file)
