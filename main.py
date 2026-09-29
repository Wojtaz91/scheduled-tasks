import requests
import smtplib
import os

email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")


api_password = "ebe7b6386ccdf15b4e9b9e41ea8289c1"
api_key = "https://api.openweathermap.org/data/2.5/forecast?"
params = {
    "lat": 50.323745,
    "lon": 18.604074,
    "appid": api_password,
    "cnt": 4,
}
response = requests.get(api_key, params=params)
a = response.status_code
print(a)
data = (response.json())
datas = False
for i in data["list"]:
     if i["weather"][0]["id"] < 600:
         datas = True


print(datas)
if datas:
    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.starttls()
    smtp.login(user=email, password=password)
    smtp.sendmail(from_addr=email, to_addrs="wojciechturalski@gmail.com", msg="Subject: Rain\n\nBedzie dzis padac")











