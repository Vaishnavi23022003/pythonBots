import requests
from flight_data import FlightData

SHEETY_URL = "https://api.sheety.co/aeffad5a770fb5eb8147b688c81c7747/flightDeals"

class DataManager:

    def __init__(self,f_name,l_name,mail):
        res = requests.get(url=f"{SHEETY_URL}/prices", headers={"Authorization": "Bearer killuavaab"})
        self.flight_data = res.json()["prices"]
        self.find_iata()
        if f_name!="":
            data={
                "user": {
                    "firstName":f_name,
                    "lastName":l_name,
                    "email":mail
                }
            }
            res=requests.post(url=f"{SHEETY_URL}/users",headers={"Authorization": "Bearer killuavaab"},json=data)
        res=requests.get(url=f"{SHEETY_URL}/users",headers={"Authorization": "Bearer killuavaab"})
        self.usr_data=[{"firstName": i["firstName"], "lastName": i["lastName"], "email": i["email"]} for i in res.json()["users"]]

    def find_iata(self):
        for i in range(len(self.flight_data)):
            self.flight_data[i]["iataCode"]=FlightData(self.flight_data[i]["city"]).city_code


