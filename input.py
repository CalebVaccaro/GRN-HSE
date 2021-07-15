import SensorLib
from time import sleep
import sys
import json

class Input(object):

    def ValidateSensors(self):

        display = SensorLib.LCD()

        # LED INIT
        LCDMonitor = display.getSensor()
        sleep(.5)
        
        # ENV Sensor INIT
        BME280 = SensorLib.BME_280().getSensor()
        sleep(.5)
        #CCS811 = SensorLib.CCS_811().getSensor()
        #sleep(.5)

        # Validated Sensors!
        SensorLib.LCD().printData("Input","Env Senrs Validated")
        sleep(.5)

    def getInput(self):
        # return RAW ENV-data to a Paired Object (CCS and BME data)
        #ccsData = SensorLib.CCS_811().getRawData()
        bmeData = SensorLib.BME_280().getRawData()
        #allInput = {"ccs": ccsData, "bme": bmeData}
        allInput = {"bme": bmeData}
        return json.dumps(allInput)