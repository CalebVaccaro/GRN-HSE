from SensorLib.BME280 import BME_280
from SensorLib.CCS811 import CCS_811
from SensorLib.lcd import LCD
#from gpiozero import LED

#hFan = LED(23)
#rFan = LED(27)

# gpioZero GPIO example:
#led.on()
#sleep(1)
#led.off()
#sleep(1)

class Output():

    def parseInput(self, newInput):
        # get data from sensors
        # parse input data
        # input into output data
        changedOutput = newInput.bme.pressure
        getNewENV(changedOutput)

    def getNewENV(self, newOutputData):
        # if drastic change
        # see which variable has drastic change
        # physics
        changedENV = newOutputData
        getNewSituation(changedENV)

    def getNewSituation(self, newENV):
        # do GPIO and/or Static Changes
        # runtimeStatus()
        # conditionalExpressions
        # write to SD Card and Print Data
        changedSituation = newENV
        setPhysicalActions(changedSituation)

    def setPhysicalActions(self, newTasks):
        changedStatus = newTasks
        setOutputStatus(changedStatus)

    def setOutputStatus(self, data):
        LCD.printData("Output", data)
        return data
