import requests
import json

url = "https://petstore.swagger.io/v2/pet/134"
headers = {
    "Content-Type": "application/json",
    "api_key": "special-key"
}

response = requests.delete(url, headers=headers)

print(f"Статус запроса: {response.status_code}")

if response.status_code == 200:
    print("Питомец успешно удалён.")
    result = response.json()
    print(json.dumps(result, indent=4))
else:
    print(f"Ошибка при удалении питомца: {response.status_code}")
    if response.content:
        print("Ответ от API:")
        print(json.dumps(response.json(), indent=4))
