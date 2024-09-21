import requests
import datetime as dt
my_lat = 39.399872
my_lng = -8.224454

parameters = {
    "lat": my_lat,
    "lng": my_lng,
    "formatted": 0
}
# the requests.get() function expects the params argument to be a dictionary.
# This is a common convention in the requests library.
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# 400 we haven't provided the required parameters
response.raise_for_status()
print(response.json()["results"]["sunrise"])

time = response.json()["results"]["sunrise"].split("T")
print(time)

time = time[1].split(":")
print(time)

hour = time[0]
print(hour)

# Comes in 24H format
time_now = dt.datetime.now()
print(time_now.hour)

