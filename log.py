import json
from time import sleep
from datetime import datetime
import SensorLib

class Log(object):

    file = None

    def LogLurk(self):
        Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        SensorLib.LCD().printData("Log","Open Log File")

    def StopLog(self):
        SensorLib.LCD().printData("Log","Stop Logging")
        sleep(1)
        Log.file.write("\n")
        Log.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S') + "\n")
        Log.file.close()

    def LogInfo(self,output, counter, calibration):

        # dump output in JSON
        print(output)
        print(counter)
        print(calibration)
        jsonData = json.dumps(str(output))

        # write to file
        if calibration:
            Log.file.write("Calibration " + str(counter) + ": " + str(jsonData) + str("\n\n"))
        else:
            Log.file.write("Data " + str(counter) + ": " + str(jsonData) + str("\n\n"))
