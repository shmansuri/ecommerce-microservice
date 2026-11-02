import httpx
import os

PRODUCT_SERVICE_URL = os.getenv('PRODUCT_SERVICE_URL', 'http://product-service:8001')

async def fetch_product_details(product_id:int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{PRODUCT_SERVICE_URL}/v1/api/products/{product_id}")
        if response.status_code == 200:
            return response.json()

        return None