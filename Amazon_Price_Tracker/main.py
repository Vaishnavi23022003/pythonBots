import requests, smtplib
from bs4 import BeautifulSoup

# this website gives history of prices
# https://camelcamelcamel.com/

product_url="https://www.amazon.in/dp/B08346545V/ref=cm_sw_r_apan_glt_fabc_2PD8NF86682TXZGWMEJV?_encoding=UTF8&psc=1"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"}
product="Samsung 253L 3 Star Inverter Frost Free Double Door Refrigerator"

res=requests.get(url=product_url,headers=headers)

soup=BeautifulSoup(res.text,"html.parser")

price=soup.find(name="span",id="priceblock_ourprice").text
price=price[1:len(price)]
price=float(price.replace(",",""))

low_cost=24200.0

if low_cost>price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        my_mail = "mymail@mail.com"
        password = "password"
        mail="reciever@mail.com"

        mssg=f"The current price of {product} is Rs {price}. \n\nBuy Now at : {product_url}"

        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=mail, msg=f"Subject:Amazon Price Alert !!!\n\n{mssg}")
