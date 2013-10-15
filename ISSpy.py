from ubidots import ApiClient
import requests


#Get variables

req_iss = requests.get('http://api.open-notify.org/iss-now.json')
dict = req_iss.json()

latlong = dict['iss_position'];

lat = latlong['latitude']
long = latlong['longitude']

print lat

#Post variables

api = ApiClient('a21ebaf64e14d195c0044fcc3b9f6dab9d653af3')
latitude = api.get_variable(id = '56799cf1231b28459f976417')
longitude = api.get_variable(id = '56799cf1231b28459f976417')
