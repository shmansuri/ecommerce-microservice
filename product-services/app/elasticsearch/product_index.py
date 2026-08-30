from app.core.elasticsearch import es_client
from elasticsearch.helpers import bulk

# INDEX_NAME ="products"

# def create_product_index():
#     if not es_client.indices.exists(index=INDEX_NAME):
#         es_client.indices.create(
#             index=INDEX_NAME,
#             mappings={
#                 "properties":{
#                     "id":{
#                         "type":"integer"
#                     },
#                     "name":{
#                         "type":"text"
#                     },
#                     "slug":{
#                         "type":"text"
#                     },
#                     "description":{
#                         "type":"text"
#                     },
#                     "category_id":{
#                         "type":"integer"
#                     },
#                     "is_active":{
#                         "type":"boolean"
#                     }
#                 }
#             }
#         )


INDEX_NAME = "products"

print("INDEX_NAME:", INDEX_NAME)

def create_product_index():
    if not es_client.indices.exists(index=INDEX_NAME):

        es_client.indices.create(
            index=INDEX_NAME,
            mappings={
                "properties": {
                    "id": {
                        "type": "integer"
                    },
                    "name": {
                        "type": "text"
                    },
                    "slug": {
                        "type": "keyword"
                    },
                    "description": {
                        "type": "text"
                    },
                    "category_id": {
                        "type": "integer"
                    },
                    "is_active": {
                        "type": "boolean"
                    }
                }
            }
        )

def index_product(product):
    es_client.index(
        index=INDEX_NAME,
        id=product.id,
        document={
            "id":product.id,
            "name": product.name,
            "slug": product.slug,
            "description": product.description,
            "category_id": product.category_id,
            "is_active": product.is_active
        }
    )


#this is for when client add product in bulk through the import or excel or pdf
def bulk_index_products(products):

    actions = []

    for product in products:

        actions.append({
            "_index": INDEX_NAME,
            "_id": product.id,
            "_source": {
                "id": product.id,
                "name": product.name,
                "slug": product.slug,
                "description": product.description,
                "category_id": product.category_id,
                "is_active": product.is_active
            }
        })

    bulk(es_client, actions)

def update_product_index(product):
    es_client.update(
        index=INDEX_NAME,
        id=product.id,
        doc={
            "id":product.id,
            'name': product.name,
            'slug':product.slug,
            "description": product.description,
            "category_id": product.category_id,
            "is_active": product.is_active

        })


def delete_product_index(product_id):
    es_client.delete(
        index=INDEX_NAME,
        id=product_id
    )

def search(query):
    response = es_client.search(
        index=INDEX_NAME,
        query={
            "multi_match":{
                'query':query,
                "fields":["name", "description"]
            }
        }
    )
    return [
        {
            "score": hit["_score"],
            **hit["_source"]
        }
        for hit in response ["hits"]["hits"]
    ]