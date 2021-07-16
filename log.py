import json
import SensorLib
from time import sleep

class Log(object):

    file = None

    def LogLurk(self):
        Log.file = open("\Documents/GRN-HSE/log/log.json", "w")
        Log.file.write("\n\n")
        Log.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        Log.file.write("\n")
        SensorLib.LCD().printData("Log","Open Log File")
        sleep(.5)

    def StopLog(self):
        SensorLib.LCD().printData("Log","Stop Logging")
        Log.file = open("\Documents/GRN-HSE/log/log.json", "a")
        Log.file.close()
        
    def LogInfo(self,data):

        # dump output in JSON
        print("Log Info")
        jsonData = json.dumps(str(data))

        # write to file
        Log.file = open("Documents/GRN-HSE/log/log.json", "a")
        Log.file.write(jsonData)