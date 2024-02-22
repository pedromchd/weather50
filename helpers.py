import requests


def lookup():
    url = ()

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None
