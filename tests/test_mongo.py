from crudmongolib.crud_mongo import MongoDBLibrary

# Test insert_documents method
def test_insert_documents():
    mongo_init = MongoDBLibrary("mongodb://localhost:27017/","mongo_test","second")
    result = mongo_init.insert_documents("C:\\PROJECTS\\ALICE3\\crud_mongo_library\\tests\\test.json")
    assert result == "Documents inserted."

# Test update_document method
def test_update_document():
    mongo_init = MongoDBLibrary("mongodb://localhost:27017/","mongo_test","second")
    result = mongo_init.update_document("C:\\PROJECTS\\ALICE3\\crud_mongo_library\\tests\\test_update.json")
    assert result.startswith("Document with id")  # Check if a document is updated or inserted

# Test delete_document method
def test_delete_document():
    mongo_init = MongoDBLibrary("mongodb://localhost:27017/","mongo_test","second")
    result = mongo_init.delete_document(7)
    assert result.startswith("Document with id") # Assuming document with id 1 doesn't exist
