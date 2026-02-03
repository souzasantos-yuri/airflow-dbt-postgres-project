import requests

api_key = "00bad4c08af28752c9a11a3604851f72"
location = "Sao Paulo"

api_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"

def fetch_data():
    print("Fetching weather data from Weatherstack API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received succesfully.")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error ocurred: {e}")
        raise

def mock_fetch_data():
        return {'request': {'type': 'City', 'query': 'Guarulhos, Brazil', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Guarulhos', 'country': 'Brazil', 'region': 'Sao Paulo', 'lat': '-23.467', 'lon': '-46.533', 'timezone_id': 'America/Sao_Paulo', 'localtime': '2026-01-31 16:53', 'localtime_epoch': 1769878380, 'utc_offset': '-3.0'}, 'current': {'observation_time': '07:53 PM', 'temperature': 29, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:45 AM', 'sunset': '06:54 PM', 'moonrise': '06:11 PM', 'moonset': '04:02 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 95}, 'air_quality': {'co': '689.85', 'no2': '34.35', 'o3': '141', 'so2': '13.25', 'pm2_5': '26.25', 'pm10': '26.25', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 10, 'wind_degree': 305, 'wind_dir': 'NW', 'pressure': 1010, 'precip': 0, 'humidity': 52, 'cloudcover': 50, 'feelslike': 32, 'uv_index': 4, 'visibility': 10, 'is_day': 'yes'}}