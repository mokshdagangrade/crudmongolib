import pymongo
import json

class MongoDBLibrary:
    def __init__(self, mongo_uri, database_name, collection_name):
        """
        Initializes MongoDB connection settings.

        Parameters:
        - mongo_uri (str): MongoDB connection URI.
        - database_name (str): Name of the database.
        - collection_name (str): Name of the collection.
        """
        self.mongo_uri = mongo_uri
        self.database_name = database_name
        self.collection_name = collection_name
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.database_name]
        self.collection = self.db[self.collection_name]

    def insert_documents(self, json_file_path):
        """
        Inserts documents into the MongoDB collection.

        Parameters:
        - json_file_path (str): Path to the JSON file containing data to be inserted.

        Returns:
        - str: Message indicating the result of the operation.
        """
        with open(json_file_path, "r") as file:
            json_data = json.load(file)

        self.collection.insert_many(json_data)
        return "Documents inserted."

    def update_document(self, json_file_path):
        """
        Updates a document in the MongoDB collection.

        Parameters:
        - document_id (str): ID of the document to be updated.
        - update_data (dict): Data to update the document with.

        Returns:
        - str: Message indicating the result of the operation.
        """
        with open(json_file_path, "r") as file:
            json_data = json.load(file)
        for document in json_data:
            # Define the unique identifier (e.g., _id)
            unique_identifier = document["id"]
            result = self.collection.update_one(
                {"id": unique_identifier},
                {"$set": document},
                upsert=True  # Insert if not present
            )

            if result.modified_count > 0:
                return (f"Document with id '{unique_identifier}' updated.")
            else:
                return (f"Document with id '{unique_identifier}' inserted.")

    def delete_document(self, document_id):
        """
        Deletes a document from the MongoDB collection.

        Parameters:
        - document_id (str): ID of the document to be deleted.

        Returns:
        - str: Message indicating the result of the operation.
        """
        result = self.collection.delete_one({"id": document_id})
        if result.deleted_count > 0:
            return f"Document with id '{document_id}' deleted."
        else:
            return f"No document found with id '{document_id}' for deletion."

    def read_data(self, query):
        """
        Reads data from the MongoDB collection based on a query.

        Parameters:
        - query (dict): MongoDB query to filter data.

        Returns:
        - list: List of documents matching the query.
        """
        return list(self.collection.find(query))
