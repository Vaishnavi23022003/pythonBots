import requests
import datetime as dt
from dateutil.relativedelta import relativedelta

TEQUILA_URL = "https://tequila-api.kiwi.com"
TEQUILA_KEY = "00000000000000"
TEQUILA_HEADER = {
    "apikey": "00000000000000000000000"
}

today=dt.datetime.now()
start_date=today.strftime("%d/%m/%Y")
six_months = today.today() + relativedelta(months=+7)
end_date=six_months.strftime("%d/%m/%Y")

class FlightSearch:

    def __init__(self, city_from_code: str, city_to_code: str):

        self.t_params = {
            "fly_from": city_from_code,
            "fly_to": city_to_code,
            "date_from": start_date,
            "date_to": end_date,
            "max_stopovers":"0"
        }

        t_res = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=TEQUILA_HEADER, params=self.t_params)

        self.price_list=[[i["price"],i["cityFrom"],i["flyFrom"],i["cityTo"],i["flyTo"],i["utc_departure"],
                          i["utc_arrival"],i["route"][0]["cityTo"]] for i in t_res.json()["data"]]

        self.price_list=[]
        self.min_price=-1

        if len(self.price_list)>0:
           self.min_price=min(self.price_list)

        if len(self.price_list)==0:
            self.t_params["max_stopovers"]="1"
            t_res = requests.get(url=f"{TEQUILA_URL}/v2/search", headers=TEQUILA_HEADER, params=self.t_params)
            self.price_list = [[i["price"], i["cityFrom"], i["flyFrom"], i["cityTo"], i["flyTo"], i["utc_departure"],
                                i["utc_arrival"],i["route"][0]["cityTo"]] for i in t_res.json()["data"]]

            if len(self.price_list) > 0:
                self.min_price = min(self.price_list)

