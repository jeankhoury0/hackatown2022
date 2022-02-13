import requests
import json
from shapely.geometry import shape, Point

from app.controllers.SmsController import SmsController

url_ordure_menage = r"https://data.montreal.ca/dataset/2df0fa28-7a7b-46c6-912f-93b215bd201e/resource/5f3fb372-64e8-45f2-a406-f1614930305c/download/collecte-des-ordures-menageres.geojson"

def _getTiming():
    try:
        res = requests.get(url_ordure_menage)
    except requests.ConnectionError:
        print("error")
        return "Connection Error"
    
    print(res)       
    return res

# return the message to the function



def getGarbageMessage(coordinates):
    to_return = ""
    res =_getTiming().json()
    # lat = "{:.7f}".format(coordinates[0])
    # long = "{:.7f}".format(float(coordinates[1]))
    # print(lat, long)
    # user_point = Point(coordinates[0], long)
    # print(user_point)
    user_point = Point(-73.6062391, 45.5333334)


    #POINT (-73.56703198244441 45.4901353921377)à
    #POINT(-73.6062391 45.5333334)
    
    for feature in res['features']:
        polygon = shape(feature['geometry'])

        if polygon.contains(user_point):
            # print(json(res))
            # to_return = feature['properties']['MESSAGE_FR']
            to_return = "entre 5 h et 8 h le mercredi de la collecte Quantité maximale acceptée :  - 360 litres par unité d'occupation pour le secteur résidentiel. - 720 litres par établissement industriel ou commercial."
            
            print("OKi doki")
            # print("\n res \n", to_return)
            # return to_return

    return to_return


