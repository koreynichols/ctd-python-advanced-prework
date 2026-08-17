import requests

def fetch_regions():
    try:
        response = requests.get("https://countries.dev/regions")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException:
        print("Unable to retrieve regions")
        return []
    
def fetch_countries():
    try:
        response = requests.get("https://countries.dev/countries")
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException:
        print("Unable to retrieve country data.")
        return []

def filter_countries(countries, region):
    filtered_countries = []
    for country in countries:
        if country["region"].lower() == region.lower():
            filtered_countries.append(country)
    return filtered_countries

def display_country(country):
    name = country.get("name")
    if name is None:
        name = "Unknown"

    population = country.get("population")
    if population is None:
        population = "N/A"

    capital = country.get("capital")
    if capital is None:
        capital = "N/A"

    area = country.get("area")
    if area is None:
        area = "N/A"

    print("\n" + name)
    print("Capital: " + str(capital))
    print("Population: " + str(population))
    print("Area: " + str(area))

def main():
    regions = fetch_regions()
    all_countries = fetch_countries()
    print("Country Explorer")
    print("================")
    print("\nAvailable regions:")

    for region in regions:
        print(region)

    region = input("\nEnter a region: ").strip()
    countries = filter_countries(all_countries, region)

    if not countries:
        print(f"No countries found for region: {region}")
        return

    print(f"\nCountries in {region}")
    print("======================")

    for country in countries:
        display_country(country)

if __name__ == "__main__":
    main()
