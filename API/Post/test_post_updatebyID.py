import requests
import json

pet_id = 23
url = f"https://petstore.swagger.io/v2/pet"
headers = {"Content-Type": "application/json"}

data = {
    "id": pet_id,
    "name": "efhghutr",
    "status": "345tj54fg"
}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(f"Статус запроса: {response.status_code}")

if response.status_code == 200:
    updated_pet_info = response.json()
    print("Информация о питомце после обновления:")
    print(json.dumps(updated_pet_info, indent=4))
else:
    print(f"Ошибка при обновлении информации о питомце: {response.status_code}")