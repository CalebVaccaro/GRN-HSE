import json
from time import sleep
from datetime import datetime
import SensorLib

class Log(object):

    file = None

    def LogLurk(self):
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "r")
        self.file.write("\n\n")
        self.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        self.file.write("\n")
        SensorLib.LCD.printData("Log","Open Log File")

    def StopLog(self):
        SensorLib.LCD.printData("Log","Stop Logging")
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        self.file.close()

    def LogInfo(self,data):
        # dump output in JSON
        print("Log Info")
        jsonData = json.dumps(str(data))

        # write to file
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        self.file.write("\nRuntime " + str(0) + " :" + str(jsonData) + str("\n") + "dt: " + datetime.today().strftime('%H:%M:%S') +"\n")


