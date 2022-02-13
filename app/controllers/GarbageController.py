import requests
import json

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
    for feature in range(len(res['features'])):
        for coordinate in res['features'][feature]['geometry']['coordinates']:
            for i in coordinate:
                if i == coordinates:
                    to_return = (res['features'][feature]
                                ['properties']['MESSAGE_FR'])
                    acc = SmsController("+14385301370", to_return)
                    acc.sendSMS()
                    print("SMS Was sent")
                    print("this is the res", to_return)
                    return to_return 
        break
    return to_return
