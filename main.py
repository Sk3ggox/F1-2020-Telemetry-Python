import pyrebase
from f1_telemetry.server import get_telemetry
import time
import os

#Enter your auth keys here
firebaseConfig = {"apiKey": "",
   "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": ""}
#Init FireBase application
firebase=pyrebase.initialize_app(firebaseConfig)
db=firebase.database()

#Prevent unnecessary spamming
prevWA = 0
prevSP = 0

if __name__ == '__main__':
    print("Server started on 20777")
    for packet, theader, mad, player in get_telemetry():
        #Check if it's a motion packet
        if theader == 0:
            #Store value as string in wa0
            wa0 = str(packet.m_frontWheelsAngle)
            #Prevent unnecessary spamming
            if prevWA != wa0:
                #Create json formatted data
                data={"frontwheelangle":wa0}
                #Send json format data to FireBase
                db.child("frontwheelangle").update(data)
                #Prevent unnecessary spamming
                prevWA = wa0
        if theader == 6:
            sp0 = str(packet.m_carTelemetryData.m_speed)
            if prevSP != sp0:
                data={"speed":sp0}
                db.child("speed").update(data)
                prevSP = sp0   
