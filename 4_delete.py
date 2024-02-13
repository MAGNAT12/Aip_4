import requests


respons = requests.delete("https://jsonplaceholder.typicode.com/posts/2")

print(respons.text)
print(respons.json())
