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

    def parseInput(self, input):
        # get data from sensors
        # parse input data
        # input into output data
        output = input.bme.pressure
        getNewENV(output)

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
        newSituation = newENV
        setPhysicalActions(newSituation)

    def setPhysicalActions(self, newTasks):
        newStatus = newTasks
        setOutputStatus(newStatus)

    def setOutputStatus(self, data):
        LCD.printData("Output", data)
