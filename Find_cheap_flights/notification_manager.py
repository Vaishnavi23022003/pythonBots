import smtplib
from flight_data import FlightData
class NotificationManager:

    def __init__(self,flight_details,usr_list):
        mssg = f"Subject:Flight Alert !!!"
        for flight in flight_details:
            mssg+=f"\n\nOnly ${flight[0]} to fly from {flight[1]}-" \
                      f"{flight[2]} to {flight[3]}-{flight[4]}, from " \
                      f"{flight[5][0:10]} to {flight[6][0:10]}."

            if flight[7] != flight[3]:
                mssg+=f"Flight has 1 stop over, via {flight[7]}."

        for user in usr_list:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                my_mail = "killuak722@gmail.com"
                password = "killu@9652killua"
                connection.login(user=my_mail, password=password)
                connection.sendmail(from_addr=my_mail, to_addrs=user["email"], msg=mssg)
                print("Success !!! 🤩")
