import json
from time import sleep
from datetime import datetime
import SensorLib

class Log(object):

    file = None
    outData = None

    def LogLurk(self):
        Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        Log.file.write("\n\n")
        Log.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        Log.file.write("\n")
        SensorLib.LCD().printData("Log","Open Log File")

    def StopLog(self):
        SensorLib.LCD().printData("Log","Stop Logging")
        sleep(1)
        Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        Log.file.close()
        
    def LogInfo(self,data, count, calibration):
        # dump output in JSON
        print("Log Info")
        jsonData = json.dumps(str(data))

        # write to file
        Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        if calibration:
            Log.file.write("Calibration " + str(count) + " :" + str(jsonData) + str("\n"))
        else:
            Log.file.write("Runtime " + str(count) + " :" + str(jsonData) + str("\n"))

