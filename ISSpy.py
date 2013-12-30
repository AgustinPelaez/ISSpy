from ubidots import ApiClient
import requests,time
from math import *


#Connect to Ubidots

api = ApiClient('a21ebaf64e14d195c0044fcc3b9f6dab9d653af3')

#Instantiate local variable from Ubidots

boston_distance = api.get_variable('525c7e69f91b2858265d746a')

#Get variables

while(1):
   req_iss = requests.get('http://api.open-notify.org/iss-now.json')
   dict = req_iss.json()
   latlong = dict['iss_position'];
   lat = latlong['latitude']
   long = latlong['longitude']

   #Calculate Distance to Boston

   my_lat = 42.3581
   my_long = 71.0636
   
   a = sin((my_lat-lat)/2)**2 + cos(lat)*cos(my_lat)*sin((my_long-long)/2)**2
   c = 2*atan2(sqrt(a),sqrt(1-a))
   d = 6378.1*c
   d = round(d,1)
   
   #Send value to Ubidots
   boston_distance.save_value({'value':d})
   time.sleep(1)
