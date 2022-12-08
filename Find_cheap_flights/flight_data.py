import requests

TEQUILA_URL = "https://tequila-api.kiwi.com"
TEQUILA_KEY = "sAY3I2JVyQJoyuPDTAq1Iy79pgA7a6Em"
TEQUILA_HEADER = {
    "apikey": "sAY3I2JVyQJoyuPDTAq1Iy79pgA7a6Em"
}


class FlightData:

    def __init__(self, city: str):
        t_res = requests.get(url=f"{TEQUILA_URL}/locations/query", headers=TEQUILA_HEADER, params={"term": city})
        self.city_code = t_res.json()["locations"][0]["code"]
