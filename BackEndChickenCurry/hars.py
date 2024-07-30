import requests
import json


'''
logging in account test
'''
#print(requests.get("http://127.0.0.1:5000/login?total=sharma,69420").content)


'''
adding account test
'''
url = "http://127.0.0.1:5000/savedata"

data = {
    "ligma": {
        "password": "666"
    }
}

response = requests.post(url, headers={"Content-Type": "application/json"}, json=data)

print("Response Code:", response.status_code)
print("Response Body:", response.json())
