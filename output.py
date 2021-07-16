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

class Output:

    def __init__(self):
        # Last Median Values
        self.lastHumidity = 0
        self.lastTemperature = 0

        # Current Median Values
        self.currentHumidity = 0
        self.currentTemperature = 0

        # High Values
        self.highHumidity = 0
        self.highTemperature = 0

        # Low Values
        self.lowHumidity = 0
        self.lowTemperature = 0

        # Array Indices for Median Calculation
        self.humidityIndex = []
        self.tempIndex = []

        self.counter = 0
        self.calibration = False

    def clearDataLists(self):
        del self.humidityIndex [:]
        del self.tempIndex [:]

    def parseQuickPacket(self, newInput, count):
        self.counter = count
        self.calibration = True

        bme = json.loads(newInput)["bme"]
        temp = json.loads(bme)["temperature"]
        humid = json.loads(bme)["humidity"]

        self.addValueToMedian(self.humidityIndex, humid)
        self.addValueToMedian(self.tempIndex, temp)

        self.setselfStatus(str("%.2f" % temp) + " " + str("%.3f" % humid))

    # get data from sensors
    # parse input data
    # input into self data
    def parseInput(self,newInput):
        
        self.calibration = False

        bme = json.loads(newInput)["bme"]
        temp = json.loads(bme)["temperature"]
        humid = json.loads(bme)["humidity"]

        humidChange = self.CalculateIndex(self.humidityIndex, humid, self.currentHumidity, self.highHumidity, self.lowHumidity, self.lastHumidity)
        tempChange = self.CalculateIndex(self.tempIndex, temp, self.currentTemperature, self.highTemperature, self.lowTemperature, self.lastTemperature)

        rawPacket = {
            "type" : "RawPacket",
            "humidStatus" : humidChange,
            "tempStatus" : tempChange,
            "humidMean" : self.currentHumidity,
            "tempMean" : self.currentTemperature,
        }

        packet = json.dumps(rawPacket)
        #print(self.currentHumidity)
        self.getNewENV(packet)


    def addValueToMedian(self, list, incomingValue):
        print(incomingValue)
        list.append(incomingValue)

    # add index to median list
    # takes 10 entries
    def CalculateIndex(self, list, incomingValue, current, high, low, last):
        list.append(incomingValue)
        self.getNewMedian(list, current, high, low, last)

    # add values in array and divide by array size
    # get high and low values
    def getNewMedian(self, list, current, high, low, last):
        # calculate new median
        current = sum(list) / len(list)
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
        self.getChangeInMedians(current, last)

    # check the change in medians
    def getChangeInMedians(self,current, last):
        # Last Median >= Current Median
        if current > last:
            print("True")
            return True
        else:
            return False

    # see which variable has drastic change
    # if drastic change
    # physics
    def getNewENV(self,newselfData):
        changedENV = json.loads(newselfData)["tempStatus"]
        self.getNewSituation(changedENV)

    # conditionalExpressions
    def getNewSituation(self,newENV):
        changedSituation = newENV
        self.setPhysicalActions(changedSituation)

    # GPIO self
    def setPhysicalActions(self,newTasks):
        changedStatus = newTasks
        self.setselfStatus(changedStatus)

    # Static self
    def setselfStatus(self,data):

        print("Data")
        print(data)
        #print("End self")

        if self.calibration is True:
            calData = "\nCalibration " + str(self.counter) + " :" + str(data) + "\ndt: " + datetime.today().strftime('%H:%M:%S') +"\n"
            Log.LogInfo(calData)
            SensorLib.LCD.printData("Cal Temp", data)
        else:
            runData = "\nRuntime " + str(self.counter) + " :" + str(data) + "\ndt: " + datetime.today().strftime('%H:%M:%S') +"\n"
            Log().LogInfo(runData)
            SensorLib.LCD.printData("Temp", data)

        # Return JSON of selfStatus and High/Low/Median Values
        #return finalself