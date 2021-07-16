import json
import SensorLib
from time import sleep

class Input:

    def __init__(self):
        self.b = SensorLib.BME_280()
        self.c = SensorLib.CCS811()
        self.l = SensorLib.LCD()

    def ValidateSensors(self):

        # LED INIT
        self.l.getSensor()
        sleep(.5)
        
        # ENV Sensor INIT
        self.b.getSensor()
        sleep(.5)
        #self.c.getSensor()
        #sleep(.5)

        # Validated Sensors!
        self.l.printData("Input","Env Senrs Validated")
        sleep(.5)

    def getInput(self):
        # return RAW ENV-data to a Paired Object (CCS and BME data)
        #ccsData =self.c.getRawData()
        bmeData = self.b.getRawData()
        #allInput = {"ccs": ccsData, "bme": bmeData}
        allInput = {"bme": bmeData}
        return json.dumps(allInput)