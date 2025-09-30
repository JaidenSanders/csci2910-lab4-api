import requests

def get_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"

    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()

        if joke_data["type"] == "single":
            print(f"Joke: {joke_data['joke']}")
        elif joke_data["type"] == "twopart":
            print(f"Setup: {joke_data['setup']}")
            print(f"Delivery: {joke_data['delivery']}")
        else:
            print("No joke found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

get_random_joke()
