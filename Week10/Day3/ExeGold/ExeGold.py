import requests



def main():
    giphy_url = "https://api.giphy.com/v1/gifs/search"
    # param = {
    #     "api_key": "dc6zaTOxFJmzC",
    #     "q": "hilarious",
    #     "limit": 20,
    #     "offset": 0,
    #     "rating": "g",
    #     "lang": "en"
    # }
    # ?q=hilarious&rating=g&api_key=dc6zaTOxFJmzC"
    response = requests.get(giphy_url, params={ "api_key": "dc6zaTOxFJmzC","q": "hilarious",})
    if response.status_code == 200:
        data = response.json()
        print(data)


if __name__ == "__main__":
    main()
