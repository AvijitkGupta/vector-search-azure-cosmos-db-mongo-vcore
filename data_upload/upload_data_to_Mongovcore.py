import os
from dotenv import load_dotenv
from pymongo import MongoClient
from ast import literal_eval
import pandas as pd

# Constants
IMAGE_FILE_COLUMN_NAME = "image_file"
DESCRIPTION_COLUMN_NAME = "description"
AUTHOR_COLUMN_NAME = "author"
TITLE_COLUMN_NAME = "title"
TECHNIQUE_COLUMN_NAME = "technique"
TYPE_COLUMN_NAME = "type"
TIMEFRAME_COLUMN_NAME = "timeframe"
VECTOR_COLUMN_NAME = "vector"

# Directories
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

# Load environment file
load_dotenv(os.path.join(parent_dir, ".env"), override=True)

# MongoDB credentials
mongo_host = os.getenv("MONGO_HOST")
mongo_user = os.getenv("MONGO_USER")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_database_name = os.getenv("MONGO_DB_NAME")
collection_name = os.getenv("MONGO_COLLECTION_NAME")

# Dataset's folder
dataset_folder = os.path.join(parent_dir, "dataset")
dataset_filepath = os.path.join(dataset_folder, "dataset_embeddings.csv")


def main():
    # Connect to MongoDB
    client = MongoClient(host=mongo_host)
    db = client[mongo_database_name]
    collection = db[collection_name]

   # Drop collection if exists
    collection.drop()

    print("Saving data to MongoDB...")
    from ast import literal_eval
    data = pd.read_csv(dataset_filepath,index_col=False,sep='\t')
    #data = data.drop('Unnamed: 0', axis=1)
    data.vector = data.vector.apply(literal_eval)

    for i in range(len(data)):
        doc_to_upload = data.loc[i].to_dict()
        collection.insert_one(doc_to_upload)
        
    #print("Document", i , "inserted successfully.")

    # Fetch all documents from collection
    num_records = collection.count_documents({})
    print(f"Number of records in the collection: {num_records}")

    print("Done!")

if __name__ == "__main__":
    main()

