import qwiic_ccs811
import time
import sys
import json

class CCS811:

    css = None

    def getSensor(self):
        print("\nSparkFun CCS811 Sensor Basic Example \n")
        mySensor = qwiic_ccs811.QwiicCcs811()

        if not mySensor.connected:
            print("CCS811 device NOT Connected", \
                  file=sys.stderr)
            return

        mySensor.begin()
        css = MySensor

    def getRawData(self):
        # Return Better Data (JSON)
        css.read_algorithm_results()
        cssData = {'co2': css.CO2 ,'tvoc': css.TVOC }
        return cssData

#if __name__ == '__main__':
#   try:
#      runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
#    print("\nEnding Basic Example")
 #   sys.exit(0)
