from flight_data import FlightData
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from logo import LOGO
import re

print(LOGO)
print("WELCOME TO KILLUA'S FLIGHT CLUB")
print("We find the best flight deals and email you.")


def check_flights(f_name, l_name, mail):
    data_manager = DataManager(f_name, l_name, mail)
    # currently only works if input is London cuz the spreadsheet has data of London only
    # flight_from = input("From where should the flight start? ").capitalize()
    flight_from = "London"
    flight_from = FlightData(flight_from).city_code
    flight_data = data_manager.flight_data
    selected_flights=[]

    for i in flight_data:
        min_price = FlightSearch(flight_from, i["iataCode"]).min_price
        try:
            if min_price[0] <= i["lowestPrice"]:
                selected_flights.append(min_price)

        except TypeError:
            continue

    # print(data_manager.usr_data)
    NotificationManager(selected_flights, data_manager.usr_data)


new_usr = input("New User? (y/n) ")

if new_usr == 'y':
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")
    mail = input("What is your email? ")
    mail2 = input("Type your email again. ")
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.match(regex, mail) and mail == mail2:
        print("You're in the club! ☺")
        check_flights(f_name, l_name, mail)

    else:
        print("Invalid mail")

else:
    check_flights("", "", "")
