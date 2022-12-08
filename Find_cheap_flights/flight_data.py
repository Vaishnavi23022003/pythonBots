import requests

TEQUILA_URL = "https://tequila-api.kiwi.com"
TEQUILA_KEY = "000000000000"
TEQUILA_HEADER = {
    "apikey": "000000000000000000000000"
}


class FlightData:

    def __init__(self, city: str):
        t_res = requests.get(url=f"{TEQUILA_URL}/locations/query", headers=TEQUILA_HEADER, params={"term": city})
        self.city_code = t_res.json()["locations"][0]["code"]
