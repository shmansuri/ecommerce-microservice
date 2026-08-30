import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

ELASTICSEARCH_URL=os.getenv("ELASTICSEARCH_URL")

print("ELASTICSEARCH_URL:", ELASTICSEARCH_URL)

es_client =Elasticsearch(
    ELASTICSEARCH_URL
)