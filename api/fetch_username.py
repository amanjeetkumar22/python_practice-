import requests

def random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    dattaa=response.json
    return dattaa

b = random_user()
print(b)