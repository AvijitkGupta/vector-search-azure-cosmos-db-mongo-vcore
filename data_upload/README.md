# Insert data to Azure Cosmos DB for Mongo vcore

## Upload images to Azure Blob Storage

Run the *[upload_images_to_blob.py](upload_images_to_blob.py)* script to upload the images to an Azure Blob Storage container using the following command from the root folder:

```bash
python data_upload/upload_images_to_blob.py
```

The process of uploading the images to Azure Blob Storage can be summarized as follows:

1. Create a new container to store the images.

2. Retrieve the filenames of the images in the dataset.

3. Upload the images in the container, utilizing multiple threads via the `ThreadPoolExecutor` class.

## Insert data to Azure Cosmos DB for Mongo vcore collection

The *[upload_data_to_Mongovcore.py](upload_data_to_Mongovcore.py)* creates a new collection in your Azure Cosmos DB for Mongo vcore instance and populates it with data. To execute the script, use the following command from the root folder:

```bash
python data_upload/upload_data_to_Mongovcore.py
```

To insert data into an Azure Cosmos DB for Mongo vcore collection, we will proceed as follows:

1. Create a table to store the filenames of the images, their embeddings, and their associated metadata. All information is saved in the CSV file created in *[data_processing/generate_embeddings.py](../data_processing/generate_embeddings.py)*.

2. Insert the data from the CSV file into the collection.
