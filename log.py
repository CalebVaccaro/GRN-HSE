import json
from time import sleep
from datetime import datetime
import SensorLib

class Log(object):

    file = None

    def LogLurk(self):
        Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "w")
        Log.file.write("\n\n")
        Log.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        Log.file.write("\n")
        SensorLib.LCD().printData("Log","Open Log File")

    def StopLog(self):
        SensorLib.LCD().printData("Log","Stop Logging")
        #Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        Log.file.close()
        
    def LogInfo(self,data):
        # dump output in JSON
        print("Log Info")
        jsonData = json.dumps(str(data))

        # write to file
        #Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        Log.file.write("\nRuntime " + str(0) + " :" + str(jsonData) + str("\n") + "dt: " + datetime.today().strftime('%H:%M:%S') +"\n")


