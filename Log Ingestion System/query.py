
from elasticsearch import Elasticsearch

# Elasticsearch connection details
es = Elasticsearch(
    hosts=["https://3d033546009e49c9af9c257ac16f4087.us-central1.gcp.cloud.es.io:9243"],
    basic_auth=("21eca12@karpagamtech.ac.in","ARUNns123@#$"),
    verify_certs=True,
    timeout=60,
)

def search_logs(query):
    # Elasticsearch search query
    search_body = {
        "query": {
            "query_string": {
                "query": query,
            }
        }
    }

    # Perform the search
    response = es.search(index="logs", body=search_body)

    # Extract and print the relevant information
    for hit in response["hits"]["hits"]:
        print("Log:", hit["_source"])

# Get user input for the search query
user_query = input("Enter your search query: ")

# Search logs based on the user input
search_logs(user_query)