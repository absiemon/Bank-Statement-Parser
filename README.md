# Bank-Statement-Parser
This project is a Python application that parses bank statement PDF files, extracts transaction data, and provides a RESTful API for accessing and querying this data.
It scans through your email and gets all the emails with subject as **My bank statement**, then gets the attached bank statement, parses it into JSON data and creates a json file called 
bank_statement_data.json.

## Info
- **Remember to use bank statement format provided in bank_statement_app -> pdfs directory.**
- **Here is the template for that pdfs that was provided in assignment.**
- [Template](https://templatelab.com/wp-content/uploads/2020/07/Bank-Statement-Template-1-TemplateLab-1.jpg)
- [Download template](https://templatelab.com/bank-statement/)
- Edit the template and send it to your email with **My bank statement** as subject. Sample is present in bank_statement_app -> pdfs.
  
## Project Overview

- **PDF Parsing:** The application uses the `pdfplumber` library to parse PDFs attached to emails received on Gmail. It looks for emails with a specific subject line indicating that the attached PDF is a bank statement. It extracts text from the PDFs.

- **API Integration:** The project implements a set of APIs for interacting with the parsed bank statement data. These APIs provide functionality to:
  - Retrieve a list of parsed transactions.
  - Search for transactions within a specific date range.
  - Get the total balance as of a specific date.

## Installation Guide

Follow these steps to set up and run the project:
1. Create a folder of your desired name.
2. Navigate to the project folder.
   ```bash
   cd projectName
   ```
3. Clone the project repository to your local machine:
   ```bash
   git clone https://github.com/absiemon/Bank-Statement-Parser.git
   ```
4. Install dependencies using pip
```bash
   pip install django
   pip install pdfplumber
   ```
5. Navigate to bank_statement_app and then startup.
6. Create a env.py file and mention
   ```bash
   email_address = "your email address"
   email_password = "your gmail password"
   ```
7. Run a python script called AccessingEmails.py. It will create a pdfs folder of bank statement pdfs.
   ```bash
   python AccessingEmails.py
   ```
8. Run a python script called ParsingPdf.py. It will create json file called bank_statement_data.json.
   ```bash
   python ParsingPdf.py
   ```
9. Navigate to the root project directory where manage.py is there. Run below command.
   ```bash
   python manage.py runserver
   ```
10. Now hit the apis to get the result.
   ```bash
   http://127.0.0.1:8000/api/bank-statements?page=1&page_size=10
   http://127.0.0.1:8000/api/bank-statements/search?start_date=mm/dd/yyyy&end_date=mm/dd/yyyy
   http://127.0.0.1:8000/api/bank-statements/search-by-date?target_date=mm/dd/yyyy
   ```
## License

[MIT](https://choosealicense.com/licenses/mit/)
