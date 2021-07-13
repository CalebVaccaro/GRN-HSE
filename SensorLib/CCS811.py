from SensorLib.CCS8112 import QwiicCcs811
import time
import sys
import json

class CCS_811(object):

    ccs = None

    def getSensor(self):
        sensor = QwiicCcs811()

        if not sensor.connected:
            print("CCS811 device NOT Connected")
            return

        CCS_811.ccs = sensor
        return CCS_811.ccs

    def getRawData(self):
        # Return Better Data (JSON)
        #time.sleep(2)
        ccs = CCS_811.ccs
        ccs.read_algorithm_results()
        ccs.read_ntc()
        ccsData = {'co2': ccs.CO2 ,'tvoc': ccs.TVOC, 'temp': ccs.temperature, 'resistance': ccs.resistance }
        return json.dumps(ccsData)

#if __name__ == '__main__':
#   try:
#      runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
#    print("\nEnding Basic Example")
 #   sys.exit(0)
