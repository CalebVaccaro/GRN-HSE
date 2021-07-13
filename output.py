import SensorLib
import json
from log import Log
#from gpiozero import LED

#hFan = LED(23)
#rFan = LED(27)

# gpioZero GPIO example:
#led.on()
#sleep(1)
#led.off()
#sleep(1)

class Output(object):

    # Last Median Values
    lastHumidity = 0
    lastPressure = 0
    lastTemperature = 0

    # Current Median Values
    currentHumidity = 0
    currentPressure = 0
    currentTemperature = 0

    # High Values
    highHumidity = 0
    highPressure = 0
    highTemperature = 0

    # Low Values
    lowHumidity = 0
    lowPressure = 0
    lowTemperature = 0

    # Array Indices for Median Calculation
    humidityIndex = []
    pressureIndex = []
    tempIndex = []

    outputData = None
    currentCounter = 0
    calibration = False

    # get data from sensors
    # parse input data
    # input into output data
    def parseInput(self,newInput, counter, calibration):
        self.currentCounter = counter
        self.calibration = calibration
        changedOutput = json.loads(newInput)["bme"]
        bmeData = json.loads(changedOutput)["temperature"]
        self.getNewENV(str("%.3f" % bmeData))

    # add index to median array
    def addValueToMedian(self,array, incomingValue):
        print(incomingValue)

    # add values in array and divide by array size
    # get high and low values
    def getNewMedian(self,array, high, low):
        return 0

    # check the change in medians
    def getChangeInMedians(self,array, lastMedian):
        # Last Median >= Current Median
        print(lastMedian)

    # see which variable has drastic change
    # if drastic change
    # physics
    def getNewENV(self,newOutputData):
        changedENV = newOutputData
        self.getNewSituation(changedENV)

    # conditionalExpressions
    def getNewSituation(self,newENV):
        changedSituation = newENV
        self.setPhysicalActions(changedSituation)

    # GPIO Output
    def setPhysicalActions(self,newTasks):
        changedStatus = newTasks
        self.setOutputStatus(changedStatus)

    # Static Output
    def setOutputStatus(self,data):
        print(data)
        print("End Output")
        self.outputData = data
        SensorLib.LCD().printData("Temp", self.outputData)
        return self.outputData

        # Return JSON of OutputStatus and High/Low/Median Values
        #return finalOutput
