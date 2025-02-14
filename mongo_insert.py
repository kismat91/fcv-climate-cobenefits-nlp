import PyPDF2
from pymongo import MongoClient
import os

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        return text


def extract_text_from_txt(txt_path, encoding='utf-8'):
    with open(txt_path, 'r', encoding=encoding, errors='replace') as file:
        return file.read()

# Function to extract project_id from the file name
def extract_project_id(file_path):
    # Get the file name without the extension
    file_name = os.path.basename(file_path).split('.')[0]
    # Extract the project_id (first part before the first underscore)
    project_id = file_name.split('_')[0]
    return project_id

# MongoDB connection
client = MongoClient('mongodb+srv://Mongo:SecureMongo@cluster0.poitw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&w=majority&tlsAllowInvalidCertificates=true')
db = client['projects_db']  # Replace with your database name
collection = db['wb_projects']

# Example usage
doc_filepath = 'P050658_Project_Appraisal_Document.txt'  # Replace with your PDF file path
# txt_path = 'P130548_Project_Appraisal_Document.txt'  # Replace with your text file path

# Extract project_id from the file name
project_id = extract_project_id(doc_filepath)  # or txt_path if using a text file

# Extract text from PDF or text file
if doc_filepath.endswith('.pdf'):
    pad_doc = extract_text_from_pdf(doc_filepath)
elif doc_filepath.endswith('.txt'):
    pad_doc = extract_text_from_txt(doc_filepath)
else:
    raise ValueError("Unsupported file format. Please provide a PDF or text file.")

# print(pad_doc)

# Insert data into MongoDB
project_data = {
    "project_id": project_id,
    "pad_doc": pad_doc
}

collection.insert_one(project_data)

print("Data inserted successfully!")