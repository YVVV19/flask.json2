from requests import get


def get_response():
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": "53.1,-0.13"}

    headers = {
        "x-rapidapi-key": "957b13c0dcmsh79cbdd448703f03p1c0563jsnb79aebaa0309",
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com",
    }

    response = get(url, headers=headers, params=querystring)
    data = response.json()
    country = data.get("location").get("country")
    city = data.get("location").get("name")
    temp = data.get("current").get("temp_c")
    condition = data.get("current").get("condition").get("text")
    return {
        "country":country,
        "city":city,
        "temperature":temp,
        "condition":condition,
    }
# print(country)
# print(city)
# print(temp)
# print(condition)
# print(data)


# {
#     "location": {
#         "name": "Boston",
#         "region": "Lincolnshire",
#         "country": "United Kingdom",
#         "lat": 53.1,
#         "lon": -0.13,
#         "tz_id": "Europe/London",
#         "localtime_epoch": 1724571507,
#         "localtime": "2024-08-25 08:38",
#     },
#     "current": {
#         "last_updated_epoch": 1724571000,
#         "last_updated": "2024-08-25 08:30",
#         "temp_c": 11.4,
#         "temp_f": 52.5,
#         "is_day": 1,
#         "condition": {
#             "text": "Sunny",
#             "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
#             "code": 1000,
#         },
#         "wind_mph": 8.1,
#         "wind_kph": 13.0,
#         "wind_degree": 220,
#         "wind_dir": "SW",
#         "pressure_mb": 1015.0,
#         "pressure_in": 29.97,
#         "precip_mm": 0.0,
#         "precip_in": 0.0,
#         "humidity": 87,
#         "cloud": 0,
#         "feelslike_c": 9.0,
#         "feelslike_f": 48.2,
#         "windchill_c": 11.9,
#         "windchill_f": 53.3,
#         "heatindex_c": 13.6,
#         "heatindex_f": 56.6,
#         "dewpoint_c": 8.0,
#         "dewpoint_f": 46.4,
#         "vis_km": 10.0,
#         "vis_miles": 6.0,
#         "uv": 4.0,
#         "gust_mph": 16.7,
#         "gust_kph": 26.8,
#     },
# }
