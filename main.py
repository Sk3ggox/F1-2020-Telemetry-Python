from f1_telemetry.server import get_telemetry
import time
import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
prevWS = 0

if __name__ == '__main__':
    print("Server started on 20777")
    for packet, theader, mad, player in get_telemetry():
        #print(theader, packet)
        if theader == 0:
            ws0 = packet.m_wheelSlip[0]
            if prevWS != ws0:
                clearConsole()
                print(ws0)
                prevWS = ws0   
