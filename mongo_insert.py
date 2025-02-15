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

# Function to extract text from a text file
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
client = MongoClient('mongodb+srv://Mongo:SecureMongo@cluster0.poitw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&tlsAllowInvalidCertificates=true')
db = client['projects_db']  # Replace with your database name
collection = db['wb_projects']

# List of file paths to process
file_paths = [
    'P072814_Project_Appraisal_Document.pdf',
    'P120207_Project_Appraisal_Document.pdf',
    'P173816_Project_Appraisal_Document.pdf',
]

# Process each file in the list
for doc_filepath in file_paths:
    try:
        # Extract project_id from the file name
        project_id = extract_project_id(doc_filepath)

        # Extract text from PDF or text file
        if doc_filepath.endswith('.pdf'):
            pad_doc = extract_text_from_pdf(doc_filepath)
        elif doc_filepath.endswith('.txt'):
            pad_doc = extract_text_from_txt(doc_filepath)
        else:
            print(f"Unsupported file format: {doc_filepath}")
            continue

        # Print the extracted text for debugging
        # print(f"Extracted text from {doc_filepath}:\n{pad_doc[:200]}...")  # Print first 200 characters

        # Insert data into MongoDB
        project_data = {
            "project_id": project_id,
            "pad_doc": pad_doc
        }

        collection.insert_one(project_data)
        print(f"Data inserted successfully for {doc_filepath}!")
    except Exception as e:
        print(f"Error processing {doc_filepath}: {e}")