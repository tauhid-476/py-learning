import requests


def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Error fetching data")
    
def fetch_random_joke():
    url="https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        joke_data = data["data"]
        return joke_data["content"]
    else:
        raise Exception("Failed to fetch a joke")



def main():
    try:
        username, country = fetch_random_user()
        print(f"Username: {username}\nCountry: {country}")

        joke = fetch_random_joke()
        print(joke)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
