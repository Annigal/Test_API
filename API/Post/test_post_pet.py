import requests
import json

url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}

data = {
    "id": 223,
    "category": {
        "id": 20,
        "name": "0438t34050"
    },
    "name": "Whiskers",
    "photoUrls": ["https://example.com/photo123.jpg"],
    "tags": [
        {
            "id": 20,
            "name": "Siamese"
        }
    ],
    "status": "available"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Питомец успешно добавлен:")
    print(f"Статус код запроса: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Ошибка при добавлении питомца: {response.status_code}")