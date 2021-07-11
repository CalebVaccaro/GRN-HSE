import qwiic_ccs811
import time
import sys
import json

class CCS_811:

    ccs = None

    def getSensor():
        print("\nSparkFun CCS811 Sensor Basic Example \n")
        mySensor = qwiic_ccs811.QwiicCcs811()

        if not mySensor.connected:
            print("CCS811 device NOT Connected", \
                  file=sys.stderr)
            return

        mySensor.begin()
        CCS_811.ccs = mySensor

    def getRawData():
        # Return Better Data (JSON)
        CCS_811.ccs.read_algorithm_results()
        ccsData = {'co2': CCS_811.ccs.CO2 ,'tvoc': CCS_811.ccs.TVOC }
        time.sleep(1)
        return json.dumps(ccsData)

#if __name__ == '__main__':
#   try:
#      runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
#    print("\nEnding Basic Example")
 #   sys.exit(0)
