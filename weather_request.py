import json
import subprocess

def install_package(package):
    subprocess.check_call(["python", "-m", "pip", "install", package])

try:
    import requests
except ImportError:
    print("requests module not found. Installing...")
    install_package("requests")
    import requests

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("playwright module not found. Installing...")
    install_package("playwright")
    from playwright.sync_api import sync_playwright

def get_cookies_with_playwright():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.msn.com/en-us/weather/forecast/")
        cookies = context.cookies()
        browser.close()
        return cookies

def fetch_weather_trends():
    try:
        with open('config.json', 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        print("Config file not found. Please ensure 'config.json' exists.")
        return

    url = "https://assets.msn.com/service/weather/weathertrends"
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "dnt": "1",
        "origin": "https://www.msn.com",
        "priority": "u=1, i",
        "referer": "https://www.msn.com/",
        "sec-ch-ua": '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-ms-gec": "652CFA092A293E9A0328BC60B2F272D3AAC79F7E4BCF5358F965166292328DD6",
        "sec-ms-gec-version": "1-131.0.2903.86",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
        "x-client-data": 'eyIxIjoiMCIsIjEwIjoiXCJNblFXVVZCK21Rak5CMnN6dFhlMVB3U3pNaTZTTXVabGpURFNpb1M0bkFJPVwiIiwiMiI6IjAiLCIzIjoiMCIsIjQiOiIyNzAxNjA3MjYwNzYyNDg5NCIsIjUiOiJcIlRxUmpmU21IR25IUnUyZURqNTJDZkFNWmlkR3lnRkJhZHFWVm1qd3E1T0k9XCIiLCI2Ijoic3RhYmxlIiwiNyI6IjMyNjQxNzUxNDQ5OSIsIjkiOiJkZXNrdG9wIn0=',
        "x-edge-shopping-flag": "1"
    }

    for location in config['locations']:
        params = {
            "apiKey": "j5i4gDqHL6nGYwx5wi5kRhXjtf2c5qgFX9fzfk0TOo",
            "cm": "en-us",
            "locale": "en-us",
            "lon": location['longitude'],
            "lat": location['latitude'],
            "units": "F",
            "user": "m-10FD438E182F66F2034E5778192767A5",
            "ocid": "msftweather",
            "includeWeatherTrends": "true",
            "includeCalendar": "false",
            "fdhead": "",
            "weatherTrendsScenarios": "TemperatureTrend,OverviewSummary,Summary,ClimateSummary",
            "days": "10",
            "insights": "1",
            "startDate": "20240201",
            "endDate": "20250131"
        }

        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            print(f"Weather trends for {location['city']}, {location['state']}:")
            print(json.dumps(data, indent=4))
        else:
            print(f"Failed to fetch weather trends for {location['city']}, {location['state']}. Status code: {response.status_code}")
            print("Attempting to retrieve cookies using Playwright...")
            cookies = get_cookies_with_playwright()
            print("Cookies retrieved:", cookies)

if __name__ == "__main__":
    fetch_weather_trends()
