import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 39.399872
MY_LONG = -8.224454
degree_of_error = 5

low_LAT = MY_LAT - degree_of_error
upper_LAT = MY_LAT + degree_of_error

low_LONG = MY_LONG - degree_of_error
upper_LONG = MY_LONG + degree_of_error

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
if low_LONG <= iss_longitude <= upper_LONG and low_LAT <= iss_latitude <= upper_LAT:
    Boolean = True
else:
    Boolean = False

print(Boolean)


# ---------------------- Get the SunRise and SunSet of my location ------------------#
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

print(sunrise, sunset, time_now.hour)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if Boolean == "True" and sunset < time_now.hour < sunrise:
        my_email = "yyyy@gmail.com"
        password = "xxx"
        b_email = "xxxx@gmail.com"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=b_email,
                msg=f"Subject:ISS MOVING BY\n\n Look Up :)"
            )
    else:
        print("ISS not moving on your Lat and Long")







