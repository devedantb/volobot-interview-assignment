import requests

response = requests.get(
    "http://localhost:8000/api/"
)  # change the localhost with a actual domain

print(response.json())
