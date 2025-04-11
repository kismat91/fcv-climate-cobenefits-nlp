import os
import pymongo
import json


def main():
    # Replace with your MongoDB connection string or set it in your environment as MONGO_CONNECTION_STRING.
    mongo_connection_string = os.getenv("MONGO_CONNECTION_STRING",
                                        "mongodb+srv://Mongo:SecureMongo@cluster0.poitw.mongodb.net/?retryWrites=true&w=majority")

    # Connect to the MongoDB client
    client = pymongo.MongoClient(mongo_connection_string)

    # Select the database (change 'projects_db' if your database name is different)
    db = client['projects_db']

    # Select the vector store mappings collection
    mappings_collection = db['vector_store_mappings']

    # Count total number of mapping documents
    total_mappings = mappings_collection.count_documents({})
    print(f"Total number of vector store mappings: {total_mappings}")

    # Retrieve and pretty-print each document
    print("\nMapping Documents:")
    for doc in mappings_collection.find():
        print("-" * 50)
        # Use json.dumps for pretty-printing; default=str handles ObjectId and datetime types.
        print(json.dumps(doc, indent=4, default=str))


if __name__ == '__main__':
    main()
