from ubidots import ApiClient
import requests
from math import *

#Get variables

req_iss = requests.get('http://api.open-notify.org/iss-now.json')
dict = req_iss.json()

latlong = dict['iss_position'];

lat = latlong['latitude']
long = latlong['longitude']

#Calculate Distance to Boston

lat2 = 42.3581
long2 = 71.0636

a = sin((lat2-lat)/2)**2 + cos(lat)*cos(lat2)*sin((long2-long)/2)**2
c = 2*atan2(sqrt(a),sqrt(1-a))
d = 6378.1*c

#Post variables

api = ApiClient('a21ebaf64e14d195c0044fcc3b9f6dab9d653afx')
latitude = api.get_variable(id = '525c7e4ef91b285823f85d5x')
longitude = api.get_variable(id = '525c7e43f91b285823f85d5x')
boston_distance = api.get_variable(id = '525c7e69f91b2858265d746x')

boston_distance.save_value({'value':d})
latitude.save_value({'value':lat})
longitude.save_value({'value':long})
