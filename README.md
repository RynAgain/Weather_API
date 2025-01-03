# Weather API Project

## Overview

This project is designed to fetch weather trends for specified locations. It uses the OpenStreetMap API to retrieve geographical coordinates and the MSN Weather API to fetch weather trends. The project is structured around two main scripts: `populate_config.py` and `weather_request.py`.

## Files and Functions

1. **populate_config.py**
   - **`get_lat_long(city, state)`**: Retrieves the latitude and longitude for a given city and state using the OpenStreetMap API.
   - **`add_location_to_config(city="Austin", state="Texas")`**: Adds the specified city and state, along with their latitude and longitude, to the `config.json` file. This function is interactive and allows users to input city and state names.

2. **weather_request.py**
   - **`install_package(package)`**: Installs a specified Python package using pip.
   - **`get_cookies_with_playwright()`**: Uses Playwright to retrieve cookies from the MSN Weather website, which may be used for API requests.
   - **`fetch_weather_trends()`**: Fetches weather trends for locations specified in the `config.json` file using the MSN Weather API. If the request fails, it attempts to retrieve cookies using Playwright.

## Usage Instructions

1. **Setup**
   - Ensure Python is installed on your system.
   - Install the required packages by running the following command:
     ```bash
     python -m pip install requests playwright
     ```

2. **Adding Locations**
   - Run `populate_config.py` to add a new location to the `config.json` file:
     ```bash
     python populate_config.py
     ```
   - You will be prompted to enter a city and state. The default values are Austin, Texas.

3. **Fetching Weather Trends**
   - Run `weather_request.py` to fetch weather trends for the locations specified in `config.json`:
     ```bash
     python weather_request.py
     ```
   - The script will print the weather trends for each location. If the request fails, it will attempt to retrieve cookies using Playwright.

## Configuration

- **config.json**: This file stores the locations for which weather trends are to be fetched. Each location includes the city, state, latitude, and longitude.

## Dependencies

- `requests`: Used for making HTTP requests to the OpenStreetMap and MSN Weather APIs.
- `playwright`: Used for retrieving cookies from the MSN Weather website.
