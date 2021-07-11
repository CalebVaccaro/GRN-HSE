import json
from time import sleep
from datetime import datetime
from SensorLib.lcd import LCD

class Log():

    file = None

    def LogLurk():
        Log.file = open("log/log.json", "a")
        LCD.printData("Log","Open Log File")

    def StopLog():
        LCD.printData("Log","Stop Logging")
        sleep(1)
        Log.file.write("\n")
        Log.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S') + "\n")
        Log.file.close()

    def LogInfo(output, counter, calibration):

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
