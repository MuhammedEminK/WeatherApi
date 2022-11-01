
import requests
from datetime import datetime
import certifi
import ssl
import geopy.geocoders
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

class Weather():
    global celsius
    global geolocator

    celsius  = lambda k: f"{(k- 273.15):.1f}" 
    ctx = ssl.create_default_context(cafile=certifi.where())
    geopy.geocoders.options.default_ssl_context = ctx
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    geolocator = Nominatim(scheme='http',user_agent="http")


    def __init__(self, key):
        self.key = key


    
    
    def hourse(self, lat, lon):
        data = []
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourlydaily&appid={self.key}"
        r = requests.get(url).json()
        for i in r["hourly"]:
            hourse = datetime.fromtimestamp(i["dt"]).hour
            temp = celsius(i["temp"])
            dc = {"time":hourse,"temp":temp}
            data.append(dc)
        return data

    def now(self, lat, lon):
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourlydaily&appid={self.key}"
        r = requests.get(url).json()
        humidity = r["current"]["humidity"]
        wind = r["current"]["wind_speed"]
        temp = celsius(k=r["current"]["temp"])
        now = datetime.fromtimestamp(r["current"]["dt"])
        dogum = datetime.fromtimestamp(r["current"]["sunrise"])
        batim = datetime.fromtimestamp(r["current"]["sunset"])
        geo = geolocator.reverse(f"{str(lat)}, {str(lon)}",timeout=None).raw
        location = f"{geo['address']['town']}, {geo['address']['province']}, {str(geo['address']['country_code']).upper()}"
        dc = {
            "location_text":location,
            "temp":temp,
            "humidity":str(humidity),
            "wind":str(wind),
        }

        return dc
















if __name__ == "__main__":
    key = "efa355ad3c0153106e4889cd4a833197"
    x = Weather(key=key, lat=41.0145, lon=28.9533)
    x.now()


  


    # url = f"https://api.openweathermap.org/data/3.0/onecall?lat=41.088&lon=29.011&exclude=hourlydaily&appid=efa355ad3c0153106e4889cd4a833197"
    # r = requests.get(url).json()
    # print(r["hourly"])


    # # for i in r["hourly"]:
    # #     print(datetime.fromtimestamp(i["dt"]))
    # #     print(i)


    # for i in r["daily"]:
    #     print(datetime.fromtimestamp(i["dt"]))
    #     print(i,"\n")



    