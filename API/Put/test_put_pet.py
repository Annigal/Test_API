import requests
import json

url = "https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}

data = {
    "id": 23958468,
    "category": {
        "id": 20,
        "name": "Asian cats"
    },
    "name": "Loki",
    "photoUrls": ["https://example.com/cat221.jpg"],
    "tags": [{
        "id": 21,
        "name": "Bengal"
    }],
    "status": "sold"
}

response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("Питомец успешно обновлён:")
    print(f"Код ответа на запрос: {response.status_code}")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Ошибка при обновлении питомца: {response.status_code}")