import phonenumbers
import opencage
import folium
from myphone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro  = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = '31b086531e104b2bb9705ceaa4a34d20'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)     

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")