import requests
from secrets import collection_id, postman_api_key

url = f'https://api.getpostman.com/collections/{collection_id}'
headers = {
    'X-Api-Key': postman_api_key
}
response = requests.request('GET', url, headers=headers)

collection = open("hello_postman_collection.json", "w")
collection.write(response.text)
collection.close()
