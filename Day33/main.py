'''
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

#response.raise_for_status()
data = response.json()['iss_position']
print(data)


longitude = data['longitude']
latitude = data['latitude']
iss_position = (longitude, latitude)
print(iss_position)
'''

import requests
from datetime import datetime

MY_LAT = 26.209820
MY_LNG = 32.768440

parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG, 
    "formatted":0
}

response = requests.get(url='http://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status() 

data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')
sunset = data['results']['sunset'].split('T')[1].split(':')
time_now = datetime.now() 



