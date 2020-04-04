import requests
from dining import*


#*************************************************************************************************************
#This is the image api from pixabay, but is limited to image search

# ***********************************************************************************************************

name = getfoodName()
print(name)

# url = "https://pixabay.com/api/?key=15869470-8d1d7a626e13a0e0c0234a63f&q="+ name + "&image_type=photo"

# response = requests.get(url)
# json_body = response.json()

# print(json_body["hits"][0]["webformatURL"])



# *************************************************************************************************************

#This is the image api from unsplash, it has great search but right now my app is in not approved

url ="https://api.unsplash.com/search/photos?query="+ name + "&client_id=sjauyr_gDNXxASXnt9fH3hCPitColEzzz8DVssM12SI"

response = requests.get(url)
json_body = response.json()

print(json_body["results"][0]["urls"]["small"])

