import requests


def getWeatherForecast(latitude, longitude):
    # https://open-meteo.com/en/docs
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&"
        f"longitude={longitude}"
        f"&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,snowfall,weather_code,wind_speed_10m,wind_direction_10m"
        f"&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,rain,weather_code,visibility,wind_speed_10m,wind_direction_10m,uv_index,is_day"
        f"&daily=weather_code,temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,sunrise,sunset,uv_index_max,precipitation_sum,rain_sum,precipitation_hours,precipitation_probability_max,wind_speed_10m_max,wind_direction_10m_dominant"
        f"&timezone=auto"
        f"&past_days=1"
    )

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None
