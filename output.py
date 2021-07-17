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
        self.l = SensorLib.LCD()
        self.o = Log()

        # Last Median Values
        self.lastHumidity = 0
        self.lastTemperature = 0

        # Current Median Values
        self.currentHumidity = 0
        self.currentTemperature = 0
        print("init")

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

        humidChange = False
        tempChange = False
        self.lastHumidity = self.currentHumidity
        self.lastTemperature = self.currentTemperature
        humidChange = self.CalculateIndex(0,self.humidityIndex, humid, self.currentHumidity, self.highHumidity, self.lowHumidity, self.lastHumidity)
        tempChange = self.CalculateIndex(1,self.tempIndex, temp, self.currentTemperature, self.highTemperature, self.lowTemperature, self.lastTemperature)

        #rint("Change")
        #print(humidChange)

        rawPacket = {
            "type" : "RawPacket",
            "humidChange" : humidChange,
            "tempChange" : tempChange,
            "humidMean" : self.currentHumidity,
            "tempMean" : self.currentTemperature,
            "lastTempMean" : self.lastTemperature,
            "lastHumidMean" : self.lastHumidity
        }

        packet = json.dumps(rawPacket)
        #print(self.currentHumidity)
        self.getNewENV(packet)


    def addValueToMedian(self, list, incomingValue):
        #print(incomingValue)
        list.append(incomingValue)

    # add index to median list
    # takes 10 entries
    def CalculateIndex(self, type, list, incomingValue, current, high, low, last):
        #list.append(incomingValue)
        return self.getNewMedian(type, list, current, high, low, last)

    # add values in array and divide by array size
    # get high and low values
    def getNewMedian(self, type, list, current, high, low, last):
        # calculate new median
        current = sum(list) / len(list)
        if type is 0:
            self.highHumidity = max(list)
            self.lowHumidity = min(list)
            
        else:
            self.lowTemperature = max(list)
            self.highTemperature = min(list)
        #high = max(list)
        #low = min(list)
        #Export Package
        # Time
        # BME:
        # Humidity
        # Humidity Change
        # Temp
        # Temp Change
        # New Status
        return self.getChangeInMedians(type, current, last)

    # check the change in medians
    def getChangeInMedians(self,type, current, last):
        # Last Median >= Current Median
        print(str(last) + " : " + str(current))
        if current > last:
            #last = current
            #print("True")
            if type is 0:
                #self.lastHumidity = last
                self.currentHumidity = current
                #print("humid")
                #print(self.lastHumidity)
                #print(self.currentHumidity)
            if type is 1:
                #self.lastTemperature = last
                self.currentTemperature = current
            return True
        else:
            #last = current
            #print("False")
            if type is 0:
                #self.lastHumidity = last
                self.currentHumidity = current
            if type is 1:
                #self.lastTemperature = last
                self.currentTemperature = current
            return False

    # see which variable has drastic change
    # if drastic change
    # physics
    def getNewENV(self,newselfData):
        changedENV = str(newselfData)
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

        #print("Data")
        print(data)
        #print("End self")

        if self.calibration is True:
            calData = "Calibration " + str(self.counter) + " :" + str(data)
            #self.o.file.write("\n")
            self.o.LogInfo(calData)
            self.o.LogInfo("dt: " + datetime.today().strftime('%H:%M:%S'))
            #self.o.file.write("\n")
            #self.o.file.write("dt: " + datetime.today().strftime('%H:%M:%S'))
            self.l.printData("Cal Temp", data)
        else:
            runData = "Runtime " + str(self.counter) + " :" + str(data)
            #self.o.file.write("\n\n")
            self.o.LogInfo(runData)
            self.o.LogInfo("dt: " + datetime.today().strftime('%H:%M:%S'))
            #self.o.file.write("\n")
            #self.o.file.write("dt: " + datetime.today().strftime('%H:%M:%S'))
            self.l.printData("Temp", data)

        # Return JSON of selfStatus and High/Low/Median Values
        #return finalself