import json
from time import sleep
from datetime import datetime
from SensorLib.lcd import LCD

class Log():

    file = None

    def LogLurk(self):
        Log.file = open("log/log.json", "a")
        LCD.printData("Log","Open Log File")

    def StopLog(self):
        LCD.printData("Log","Stop Logging")

    def LogInfo(self, output, calibration):
        jsonData = json.dumps(str(output))
        if calibration:
            Log.file.write("Calibration" + jsonData + str("\n\n"))
        else:
            Log.file.write(jsonData + str("\n\n"))
