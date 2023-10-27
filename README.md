# Bank-Statement-Parser
This project is a Python application that parses bank statement PDF files, extracts transaction data, and provides a RESTful API for accessing and querying this data.
It scans through your email and gets all the emails with subject as bank statement, then gets the attached bank statement, parses it into JSON data and creates a json file called 
bank_statement_data.json.

## Project Overview

- **PDF Parsing:** The application uses the `pdfplumber` library to parse PDFs attached to emails received on Gmail. It looks for emails with a specific subject line indicating that the attached PDF is a bank statement. It extracts text from the PDFs.

- **API Integration:** The project implements a set of APIs for interacting with the parsed bank statement data. These APIs provide functionality to:
  - Retrieve a list of parsed transactions.
  - Search for transactions within a specific date range.
  - Get the total balance as of a specific date.

## Installation Guide

Follow these steps to set up and run the project:
2. Create a folder of your desired name.
3. Navigate to the project folder.
   ```bash
   cd projectName
   ```
3. Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/absiemon/Bank-Statement-Parser.git
   ```
