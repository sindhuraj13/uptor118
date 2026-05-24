import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "size": 1900
}

response = requests.post(url, json=data)
print(response)
print(response.json())