import requests

# insert your real key here!

def api_get_wearher(lat: str, lon: str) -> dict:
    access_key = "1ba97666-05f8-4091-b14b-8d08cba1b7bb"
    headers = {
        "X-Yandex-API-Key": access_key
    }

    query = query = f"""
{{
  weatherByPoint(request: {{ lat: {lat}, lon: {lon} }}) {{
    now {{
      temperature
    }}
  }}
}}
"""

    response = requests.post('https://api.weather.yandex.ru/graphql/query', headers=headers, json={'query': query})
    return response.json()


def api_geo_city(city_name: str) -> dict:
    headers = {"Content-Type": "application/json", "Accept": "application/json", "Authorization": "Token 3bdbe0e988d764f9683f3ed19dfc5afd58b1f8f1", "X-Secret": "7fccba51aa48103decca5f64a3683b1f23ae3a8a"}
    data = []
    data.append(city_name)
    response = requests.post(url="https://cleaner.dadata.ru/api/v1/clean/address", headers=headers, json=data)
    return response.json()



def api_city(ip: str) -> dict:
    headers = { "Accept": "application/json", "Authorization": "Token 3bdbe0e988d764f9683f3ed19dfc5afd58b1f8f1"}
    url = f"http://suggestions.dadata.ru/suggestions/api/4_1/rs/iplocate/address?ip={ip}"
    response = requests.get(url=url, headers=headers)
    return response.json()

