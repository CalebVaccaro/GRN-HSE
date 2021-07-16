import json
import SensorLib
from time import sleep
from datetime import datetime

class Log:

    def __init__(self):
        self.file = None

    def LogLurk(self):
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "w")
        self.file.write("\n\n")
        self.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        self.file.write("\n")
        SensorLib.LCD.printData("Log","Open Log File")
        sleep(.5)

    def StopLog(self):
        SensorLib.LCD.printData("Log","Stop Logging")
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        self.file.close()
        
    def LogInfo(self,data):

        # dump output in JSON
        jsonData = json.dumps(str(data))

        # write to file
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        self.file.write(jsonData)