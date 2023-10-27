import imaplib
import email
import os
from env import email_address, password


imap_server = "imap.gmail.com"

imap = imaplib.IMAP4_SSL(imap_server, 993)
imap.login(email_address, password)

imap.select("Inbox")

#getting emails ids of emails whose SUBJECT bank statement
typ, email_ids = imap.search(None, 'SUBJECT "My bank statement"')

#mentioning directory to save the pdf files
base_dir = os.path.dirname(os.path.abspath(__file__))
pdfs_directory = os.path.join(base_dir, '../pdfs')

# Checking if the directory exists, if not, creating it
if not os.path.exists(pdfs_directory):
    os.mkdir(pdfs_directory)

for email_id in email_ids[0].split():
    _, data = imap.fetch(email_id, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    
    # Extracting and processing attachments (PDFs)
    for part in message.walk():
        content_type = part.get_content_type()
        content_disposition = str(part.get("content-disposition"))

        if "attachment" in content_disposition:
            filename = part.get_filename()
            if filename:
                file_path = os.path.join(pdfs_directory, filename)
                with open(file_path, "wb") as pdf_file:
                    pdf_file.write(part.get_payload(decode=True))
                print(f"Saved PDF attachment: {filename} to {file_path}")
