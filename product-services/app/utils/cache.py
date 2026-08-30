from app.core.redis import redis_client
import json
def get_cache(key:str):
    data = redis_client.get(key)
    if data:
        print(f"CACHE HIT: {key}")
        return json.loads(data)
    print(f"CACHE MISS: {key}")
    return None

def set_cache(key:str, value:str, expire:int = 300):
    redis_client.setex(key, expire, json.dumps(value, default=str))

def delete_cache(key:str):
    redis_client.delete(key)
