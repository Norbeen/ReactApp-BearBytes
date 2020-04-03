import requests
from dining import*


name = getfoodName()
print(name)

url = "https://pixabay.com/api/?key=15869470-8d1d7a626e13a0e0c0234a63f&q="+ name + "&image_type=photo"

response = requests.get(url)
json_body = response.json()

print(json_body["hits"][0]["webformatURL"])