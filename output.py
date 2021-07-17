import json
import SensorLib
from log import Log
from datetime import datetime
from gpio import GPIO

class Output:

    def __init__(self):
        self.l = SensorLib.LCD()
        self.o = Log()
        self.g = GPIO()

        # Last Median Values
        self.lastHumidity = 0
        self.lastTemperature = 0
        self.lastRPiTemp = 0

        # Current Median Values
        self.currentHumidity = 0
        self.currentTemperature = 0
        self.currentRPiTemp = 0

        # High Values
        self.highHumidity = 0
        self.highTemperature = 0
        self.highRPiTemp = 0

        # Low Values
        self.lowHumidity = 0
        self.lowTemperature = 0
        self.lowTempRPiTemp= 0

        # Array Indices for Median Calculation
        self.humidityIndex = []
        self.tempIndex = []
        self.RPiTempIndex = []

        self.counter = 0
        self.calibration = False

    def clearDataLists(self):
        del self.humidityIndex [:]
        del self.tempIndex [:]
        del self.RPiTempIndex [:]

    def parseQuickPacket(self, newInput, count):
        self.counter = count
        self.calibration = True

        # load json data
        bme = json.loads(newInput)["bme"]
        temp = json.loads(bme)["temperature"]
        humid = json.loads(bme)["humidity"]
        rpi = json.loads(newInput)["rPi"]

        self.addValueToMedian(self.humidityIndex, humid)
        self.addValueToMedian(self.tempIndex, temp)
        self.addValueToMedian(self.RPiTempIndex, rpi)

        trimHumid = str("%.5f" % humid)
        trimTemp = str("%.2f" % temp)

        quickPacket = {
            "type" : "QuickPacket",
            "humidity" : trimHumid,
            "temp" : trimTemp,
            "dateTime" : datetime.today().strftime('%H:%M:%S')
        }

        packet = json.dumps(quickPacket)
        self.setselfStatus(packet)

    # get data from sensors
    # parse input data
    # input into self data
    def parseInput(self,newInput):

        # Set Variables for Mean Calculation
        self.calibration = False
        humidChange = False
        tempChange = False

        # Parse JSON
        bme = json.loads(newInput)["bme"]
        temp = json.loads(bme)["temperature"]
        humid = json.loads(bme)["humidity"]
        rpi = json.loads(newInput)["rPi"]

        # Save Last Values
        self.lastHumidity = self.currentHumidity
        self.lastTemperature = self.currentTemperature

        # Calculate Variable Mean Changes
        humidChange = self.CalculateIndex(0,self.humidityIndex, humid, self.currentHumidity, self.highHumidity, self.lowHumidity, self.lastHumidity)
        tempChange = self.CalculateIndex(1,self.tempIndex, temp, self.currentTemperature, self.highTemperature, self.lowTemperature, self.lastTemperature)
        rpiChange = self.CalculateIndex(2,self.RPiTempIndex, rpi, self.currentRPiTemp, self.highRPiTemp, self.lowTempRPiTemp, self.lastRPiTemp)

        #Export Package
        # Time
        # BME:
        # Humidity
        # Humidity Change
        # Temp
        # Temp Change
        # New Status
        rawPacket = {
            "type" : "RawPacket",
            "humidChange" : humidChange,
            "tempChange" : tempChange,
            "rpiChange" : rpiChange,
            "humidMean" : str("%.5f" % self.currentHumidity),
            "tempMean" : str("%.2f" % self.currentTemperature),
            "lastTempMean" : str("%.2f" % self.lastTemperature),
            "lastHumidMean" : str("%.5f" % self.lastHumidity),
            "rpiTemp" : str("%.2f" % self.currentRPiTemp),
            "dateTime" : datetime.today().strftime('%H:%M:%S')
        }

        packet = json.dumps(rawPacket)
        self.getNewENV(packet)

    def addValueToMedian(self, list, incomingValue):
        list.append(incomingValue)

    # add index to median list
    # takes 10 entries
    def CalculateIndex(self, type, list, incomingValue, current, high, low, last):
        self.addValueToMedian(list,incomingValue)
        return self.getNewMedian(type, list, current, high, low, last)

    # add values in array and divide by array size
    # get high and low values
    def getNewMedian(self, type, list, current, high, low, last):
       
        # calculate new median
        current = sum(list) / len(list)
        maxIndex = max(list)
        minIndex = min(list)

        if type is 0:
            self.highHumidity = maxIndex
            self.lowHumidity = minIndex
        if type is 1:
            self.lowTemperature = maxIndex
            self.highTemperature = minIndex
        if type is 2:
            self.lowTempRPiTemp = maxIndex
            self.highRPiTemp = minIndex

        return self.getChangeInMedians(type, current, last)

    # check the change in medians
    def getChangeInMedians(self,type, current, last):

        # Last Median >= Current Median
        validate = current > last

        if type is 0:
            self.currentHumidity = current
        if type is 1:
            self.currentTemperature = current
        if type is 2:
            self.currentRPiTemp = current

        return validate
            
    # see which variable has drastic change
    # if drastic change
    # physics
    def getNewENV(self,newselfData):

        # create new enviroment tuple
        hChange = json.loads(newselfData)["humidChange"]
        tChange = json.loads(newselfData)["tempChange"]
        rChange = json.loads(newselfData)["rpiChange"]
        changedENV = (hChange,tChange,rChange)

        # Export Better Packet
        self.setselfStatus(str(newselfData))
        self.setPhysicalActions(changedENV)

    # GPIO self
    def setPhysicalActions(self,newTasks):

        # get each action needed
        humidAction = newTasks[0]
        tempAction = newTasks[1]
        rpiAction = newTasks[2]

        #self.g.rPiFanAction(tempAction)
        self.g.humidityFanAction(humidAction)
        #self.g.tempFanAction(tempAction)
        self.g.rPiFanAction(rpiAction)
        
    # Print and Log Incoming Data
    def setselfStatus(self,data):

        self.o.LogInfo(data)
        d = json.loads(data)

        if self.calibration is True:
            h = d["humidity"]
            t = d["temp"]
            display = "Temp: " + str(t) + " Humid: " + str(h)
            
            self.l.printData("RT", display)
        else:
            h = d["humidChange"]
            t = d["tempChange"]
            display = "TChange: " + str(t) + " HChange: " + str(h)

            self.l.printData("CX", display)

   