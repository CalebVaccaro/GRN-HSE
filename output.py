from SensorLib.BME280 import BME_280
from SensorLib.CCS811 import CCS_811
from SensorLib.lcd import LCD
import json
#from gpiozero import LED

#hFan = LED(23)
#rFan = LED(27)

# gpioZero GPIO example:
#led.on()
#sleep(1)
#led.off()
#sleep(1)

class Output():

    def parseInput(newInput):
        # get data from sensors
        # parse input data
        # input into output data
        changedOutput = json.loads(newInput)["bme"]
        bmedata = json.loads(changedOutput)["temperature"]
        Output.getNewENV(bmedata)

    def getNewENV(newOutputData):
        # if drastic change
        # see which variable has drastic change
        # physics
        changedENV = newOutputData
        Output.getNewSituation(changedENV)

    def getNewSituation(newENV):
        # conditionalExpressions
        changedSituation = newENV
        Output.setPhysicalActions(changedSituation)

    def setPhysicalActions(newTasks):
        # GPIO Output
        changedStatus = newTasks
        Output.setOutputStatus(changedStatus)

    def setOutputStatus(data):
        # Static Output
        LCD.printData("Output", data)
        print(data)
        return data
