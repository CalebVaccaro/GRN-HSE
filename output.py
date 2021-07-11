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

    # Last Median Values
    lastHumidity = 0
    lastPressure = 0
    lastTemperature = 0
    lastTVOC = 0
    lastC02 = 0

    # Current Median Values
    currentHumidity = 0
    currentPressure = 0
    currentTemperature = 0
    currentTVOC = 0
    currentC02 = 0

    # High Values
    highHumidity = 0
    highPressure = 0
    highTemperature = 0
    highTVOC = 0
    highC02 = 0

    # Low Values
    lowHumidity = 0
    lowPressure = 0
    lowTemperature = 0
    lowTVOC = 0
    lowC02 = 0

    # Array Indices for Median Calculation
    humidityIndex = []
    pressureIndex = []
    tempIndex = []
    tvocIndex = []
    co2Index = []

    # get data from sensors
    # parse input data
    # input into output data
    def parseInput(newInput):
        changedOutput = json.loads(newInput)["ccs"]
        bmedata = json.loads(changedOutput)["co2"]
        Output.getNewENV(bmedata)

    # add index to median array
    def addValueToMedian(array, incomingValue):
        print(incomingValue)

    # add values in array and divide by array size
    # get high and low values
    def getNewMedian(array, high, low):
        return 0

    # check the change in medians
    def getChangeInMedians(array, lastMedian):
        # Last Median >= Current Median
        print(lastMedian)

    # see which variable has drastic change
    # if drastic change
    # physics
    def getNewENV(newOutputData):
        changedENV = newOutputData
        Output.getNewSituation(changedENV)

    # conditionalExpressions
    def getNewSituation(newENV):
        changedSituation = newENV
        Output.setPhysicalActions(changedSituation)

    # GPIO Output
    def setPhysicalActions(newTasks):
        changedStatus = newTasks
        Output.setOutputStatus(changedStatus)

    # Static Output
    def setOutputStatus(data):
        LCD.printData("Output", data)
        print(data)

        # Return JSON of OutputStatus and High/Low/Median Values
        return data
