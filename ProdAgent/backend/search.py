from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

def search_similar_products(query: str) -> list:
    client = SearchClient(
        azure_search_key=os.getenv("AZURE_SEARCH_KEY"),
        endpoint=os.getenv("AZURE_SEARCH_ENDPOINT"),
        index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
        credential=AzureKeyCredential(os.getenv("AZURE_SEARCH_KEY"))
    )
    results = client.search(query, top=3)
    return [doc["chunk"] for doc in results]

