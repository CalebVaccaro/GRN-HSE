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
        self.ccs = mySensor

    def getRawData(self):
        # Return Better Data (JSON)
        #time.sleep(2)
        self.ccs.read_algorithm_results()
        self.ccs.read_ntc()
        ccsData = {'co2': self.ccs.CO2 ,'tvoc': self.ccs.TVOC, 'temp': self.ccs.temperature, 'resistance': self.ccs.resistance }
        return json.dumps(ccsData)

#if __name__ == '__main__':
#   try:
#      runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
#    print("\nEnding Basic Example")
 #   sys.exit(0)
