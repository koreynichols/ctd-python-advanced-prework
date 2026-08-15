import requests

def fetch_country(country):
    response = requests.get("https://countries.dev/alpha/" + country)
    data = response.json()
    print(data)

def main():
    fetch_country("US")

if __name__ == "__main__":
    main()
