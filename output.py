import json
import SensorLib
from log import Log
from datetime import datetime
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
    # lastPressure = 0
    lastHumidity = 0
    lastTemperature = 0

    # Current Median Values
    # currentPressure = 0
    currentHumidity = 0
    currentTemperature = 0

    # High Values
    # highPressure = 0
    highHumidity = 0
    highTemperature = 0

    # Low Values
    # lowPressure = 0
    lowHumidity = 0
    lowTemperature = 0

    # Array Indices for Median Calculation
    # pressureIndex = [0] * 10 
    humidityIndex = []
    tempIndex = []

    counter = 0
    calibration = False

    def clearDataLists():
        Output.humidityIndex.clear()
        Output.tempIndex.clear()

    def parseQuickPacket(self, newInput, count):
        Output().counter = count
        Output().calibration = True

        bme = json.loads(newInput)["bme"]
        temp = json.loads(bme)["temperature"]
        humid = json.loads(bme)["humidity"]

        Output().addValueToMedian(Output.humidityIndex, humid)
        Output().addValueToMedian(Output.tempIndex, temp)

        Output().setOutputStatus(str("%.2f" % temp) + " " + str("%.3f" % humid))

    # get data from sensors
    # parse input data
    # input into output data
    def parseInput(self,newInput):
        
        Output().calibration = False

        bme = json.loads(newInput)["bme"]
        temp = json.loads(bme)["temperature"]
        humid = json.loads(bme)["humidity"]

        humidChange = Output().CalculateIndex(Output.humidityIndex, humid, Output.currentHumidity, Output.highHumidity, Output.lowHumidity, Output.lastHumidity)
        tempChange = Output().CalculateIndex(Output.tempIndex, temp, Output.currentTemperature, Output.highTemperature, Output.lowTemperature, Output.lastTemperature)

        rawPacket = {
            "type" : "RawPacket",
            "humidStatus" : humidChange,
            "tempStatus" : tempChange,
            "humidMean" : Output.currentHumidity,
            "tempMean" : Output.currentTemperature,
        }

        packet = json.dumps(rawPacket)
        Output().getNewENV(packet)


    def addValueToMedian(self, list, incomingValue):
        list.append(incomingValue)

    # add index to median list
    # takes 10 entries
    def CalculateIndex(self, list, incomingValue, current, high, low, last):
        list.append(incomingValue)
        Output().getNewMedian(list, current, high, low, last)

    # add values in array and divide by array size
    # get high and low values
    def getNewMedian(self, list, current, high, low, last):
        # calculate new median
        current = sum(list) / list.count()
        high = max(list)
        low = min(list)
        #Export Package
        # Time
        # BME:
        # Humidity
        # Humidity Change
        # Temp
        # Temp Change
        # New Status
        Output().getChangeInMedians(current, last)

    # check the change in medians
    def getChangeInMedians(self,current, last):
        # Last Median >= Current Median
        if current > last:
            return True
        else:
            return False

    # see which variable has drastic change
    # if drastic change
    # physics
    def getNewENV(self,newOutputData):
        changedENV = json.loads(newOutputData)["tempStatus"]
        Output().getNewSituation(changedENV)

    # conditionalExpressions
    def getNewSituation(self,newENV):
        changedSituation = newENV
        Output().setPhysicalActions(changedSituation)

    # GPIO Output
    def setPhysicalActions(self,newTasks):
        changedStatus = newTasks
        Output().setOutputStatus(changedStatus)

    # Static Output
    def setOutputStatus(self,data):

        print(data)
        print("End Output")

        if Output.calibration is True:
            calData = "\nCalibration " + str(Output.counter) + " :" + str(data) + str("\n") + "dt: " + datetime.today().strftime('%H:%M:%S') +"\n"
            Log().LogInfo(calData)
            SensorLib.LCD().printData("Cal Temp", data)
        else:
            runData = "\nRuntime " + str(Output.counter) + " :" + str(data) + str("\n") + "dt: " + datetime.today().strftime('%H:%M:%S') +"\n"
            Log().LogInfo(runData)
            SensorLib.LCD().printData("Temp", data)

        # Return JSON of OutputStatus and High/Low/Median Values
        #return finalOutput