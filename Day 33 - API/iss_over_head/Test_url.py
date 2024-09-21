import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# this method tell raises an exception for us, and print what is the http status, and it's meaning
response.raise_for_status()

data = response.json()
print(f"the response from our request is:\n {data} \n")
data = response.json()["iss_position"]
print(f"The value for the key iss_position is:\n {data} \n")

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]
print(f"The longitude and latitude of the iss_position are:\n {longitude} and {latitude}\n")

iss_position = (longitude, latitude)
print(iss_position)
