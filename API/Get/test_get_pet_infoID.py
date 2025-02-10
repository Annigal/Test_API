import requests
import json

pet_id = 113
url = f"https://petstore.swagger.io/v2/pet/{pet_id}"
headers = {"Content-Type": "application/json"}

response = requests.get(url, headers=headers)

print(f"Статус запроса: {response.status_code}")

if response.status_code == 200:
    pet_info = response.json()
    print("Информация о питомце:")
    print(json.dumps(pet_info, indent=4))
else:
    print(f"Ошибка при получении информации о питомце: {response.status_code}")