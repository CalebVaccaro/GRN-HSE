from SensorLib.BME280 import BME_280
from SensorLib.CCS811 import CCS_811
from SensorLib.lcd import LCD
from time import sleep
import sys
import json

class Input():

    def ValidateSensors(self):

        # LED INIT
        LCDMonitor = LCD.getSensor()

        # ENV Sensor INIT
        BME280 = BME_280.getSensor()
        sleep(.5)
        CCS811 = CCS_811.getSensor()
        sleep(.5)

        # Validated Sensors!
        LCD.printData("Input","Env Sensors Validated")

    def getInput(self):
        # return RAW ENV-data to a Paired Object (CCS and BME data)
        cssData = CCS_811.getRawData()
        bmeData = BME_280.getRawData()
        allInput = {"css": cssData, "bme": bmeData}
        return json.dumps(allInput)
