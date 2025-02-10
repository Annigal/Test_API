import requests
import json

status = "2492"
url = "https://petstore.swagger.io/v2/pet/findByStatus"
params = {"status": status}
headers = {"Content-Type": "application/json"}

response = requests.get(url, headers=headers, params=params)

print(f"Статус код ответа: {response.status_code}")

if response.status_code == 200:
    pets_info = response.json()
    print("Ответ от API:")
    print(json.dumps(pets_info, indent=4))

    if pets_info:
        print(f"Питомцы со статусом '{status}':")
        print(json.dumps(pets_info, indent=4))
    else:
        print(f"Нет питомцев с таким статусом '{status}'.")
else:
    print(f"Ошибка при поиске питомцев: {response.status_code}")