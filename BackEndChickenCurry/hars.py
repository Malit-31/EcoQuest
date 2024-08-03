import requests
import json


'''
logging in account test
'''
#print(requests.get("http://127.0.0.1:5000/login?total=sharma,69420").content)


'''
adding account test
'''
# url = "http://127.0.0.1:5000/savedata"

# data = {
#     "liga": {
#         "password": "66"
#     }
# }

# response = requests.post(url, headers={"Content-Type": "application/json"}, json=data)

# print("Response Code:", response.status_code)
# print("Response Body:", response.json())

'''
adding points
'''
# url = "http://127.0.0.1:5000/addpoints"
# data = {
#     "username": "ligma",
#     "points": 10
# }
# response = requests.post(url, headers={"Content-Type": "application/json"}, json=data)

# print("Response Code:", response.status_code)
# print("Response Body:", response.json())

'''
getting points
'''
url = "http://127.0.0.1:5000/getpoints"
params = {
    "username": "ligma"
}
response = requests.get(url, params=params)

print("Response Code:", response.status_code)
print("Response Body:", response.json())