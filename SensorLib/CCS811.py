
from SensorLib.CCS8112 import QwiicCcs811
import time
import sys
import json

class CCS_811(object):

    ccs = None

    def getSensor(self):
        mySensor = QwiicCcs811()

        if not mySensor.connected:
            print("CCS811 device NOT Connected")
            return

        mySensor.begin()
        CCS_811.ccs = mySensor

    def getRawData(self):
        # Return Better Data (JSON)
        #time.sleep(2)
        CCS_811.ccs.read_algorithm_results()
        CCS_811.ccs.read_ntc()
        ccsData = {'co2': CCS_811.ccs.CO2 ,'tvoc': CCS_811.ccs.TVOC, 'temp': CCS_811.ccs.temperature, 'resistance': CCS_811.ccs.resistance }
        return json.dumps(ccsData)

#if __name__ == '__main__':
#   try:
#      runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
#    print("\nEnding Basic Example")
 #   sys.exit(0)