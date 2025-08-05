import os
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient
import streamlit as st

load_dotenv()

AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
AZURE_STORAGE_CONTAINER = os.getenv("AZURE_STORAGE_CONTAINER")

st.title("File Upload to Azure Blob Storage")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    try:
        BlobServiceClient = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        container_client = BlobServiceClient.get_container_client(AZURE_STORAGE_CONTAINER)
        blob_client = container_client.get_blob_client(uploaded_file.name)

        # Upload the file to Azure Blob Storage
        blob_client.upload_blob(uploaded_file, overwrite=True)
        
        st.success("File uploaded successfully.")
    except Exception as e:
        st.error(f"An error occurred: {e}")


try:
    BlobServiceClient = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    container_client = BlobServiceClient.get_container_client(AZURE_STORAGE_CONTAINER)
    blob_client = container_client.get_blob_client("test.jpg")

    # File upload logic can be added here
    with open(r"C:\Users\User\Desktop\KTds실습\test.jpg", "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
    
    print("File uploaded successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
