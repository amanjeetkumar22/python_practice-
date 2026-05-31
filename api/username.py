import requests

def random_user():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response=requests.get(url)
    dataa = response.json()
    
    if dataa["success"] and "data" in dataa:
        user_data = dataa["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username,country = random_user()
        print(f"Username:{username}\n Country:{country}")
        
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()