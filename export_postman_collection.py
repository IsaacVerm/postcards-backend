import requests
url = 'https://api.getpostman.com/collections/1846230-2aaa8819-bc85-48a2-8dd2-bf356d5b5dfd'
headers = {
    'X-Api-Key': '13f6b1bf0e8b4333958d55348c784be0'
}
response = requests.request('GET', url, headers=headers)
print(response.text)

collection = open("hello_postman_collection.json", "w")
collection.write(response.text)
collection.close()
