import requests
import json

pet_id = 2
image_path = r"C:\Users\yiun5\Downloads\cat2.jpg"
url = f"https://petstore.swagger.io/v2/pet/{pet_id}/uploadImage"

files = {'file': open(image_path, 'rb')}
response = requests.post(url, files=files)
files['file'].close()

if response.status_code == 200:
    result = response.json()
    print("Ответ от API:")
    print(json.dumps(result, indent=4))
else:
    print(f"Ошибка при загрузке изображения: {response.status_code}")