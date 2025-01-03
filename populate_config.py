import json
import requests

def get_lat_long(city, state):
    geocode_url = "https://nominatim.openstreetmap.org/search"
    geocode_params = {
        "q": f"{city}, {state}",
        "format": "json",
        "limit": 1
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(geocode_url, params=geocode_params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
        else:
            print("No data found for the location.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return None, None

def add_location_to_config(city="Austin", state="Texas"):
    lat, lon = get_lat_long(city, state)
    if lat is None or lon is None:
        print("Could not find the location. Please check the city and state names.")
        return

    location_data = {
        "city": city,
        "state": state,
        "latitude": lat,
        "longitude": lon
    }

    try:
        with open('config.json', 'r+') as file:
            config = json.load(file)
            config['locations'].append(location_data)
            file.seek(0)
            json.dump(config, file, indent=4)
        print(f"Added {city}, {state} to config.")
    except FileNotFoundError:
        print("Config file not found. Please ensure 'config.json' exists.")

if __name__ == "__main__":
    city = input("Enter the city (default: Austin): ") or "Austin"
    state = input("Enter the state (default: Texas): ") or "Texas"
    add_location_to_config(city, state)
