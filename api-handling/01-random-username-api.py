import requests

def fetchInfo():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if ("data" in data and data['success']):
        user_data = data['data']
        
        name = f"{user_data['name']['first']} {user_data['name']['last']}"
        user_name = f"{user_data['login']['username']}"
        user_gender = f"{user_data['gender']}"
        user_age = f"{user_data['dob']['age']}"
        return (name, user_name, user_gender, user_age)
    else:
        raise Exception("Falied to fetch information")

def main():
    try:
        (name, user_name, user_gender, user_age) = fetchInfo()
        print(f"Name : {name}")
        print(f"Username : {user_name}")
        print(f"User gender : {user_gender}")
        print(f"User Age : {user_age}")

    except Exception as e:
        print(str(e))
    finally:
        print("Done.......")

if __name__ == "__main__":
    main()