import requests
from models import *
import time

def reccursiveReastaurant(latitude,longitude,radius,restaurantList, nextPageToken = None):
    f = open("GooglePlacesAPIKey.txt", "r")
    apiKey = f.readline()
    f.close()
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    PARAMS = {"key":str(apiKey),
    "location": str(latitude)+ "," + str(longitude),
    "radius": int(radius),
    "type": "restaurant",
    "rankby": "prominence",
    "opennow": "true"
    }
    print("Lat",latitude)
    if nextPageToken != None:
        PARAMS["pagetoken"] = str(nextPageToken)
    resp = requests.get(url,params = PARAMS)
    data = resp.json()
    for restaurant in data["results"]:
        restaurantList.append(Restaurant(name = restaurant["name"]))
    if "next_page_token" in data:
        time.sleep(2)
        return reccursiveReastaurant(latitude,longitude,radius,restaurantList,data["next_page_token"])
    else:
        return restaurantList
