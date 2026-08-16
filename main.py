import requests

def fetch_regions():
    response = requests.get("https://countries.dev/regions")
    data = response.json()
    return data;

def fetch_country(region):
    response = requests.get("https://countries.dev/region/" + region)
    data = response.json()
    print(data)

def main():
    regions = fetch_regions()
    print("Country Explorer")
    print("================")
    print("\nAvailable regions:")

    for region in regions:
        print(region)

    region = input("\nEnter a region: ")
    print(f"\nCountries in {region}")
    print("======================")
    
if __name__ == "__main__":
    main()
