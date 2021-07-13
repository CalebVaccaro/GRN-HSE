import json
from time import sleep
from datetime import datetime
import SensorLib

class Log(object):

    file = None

    def LogLurk(self):
<<<<<<< HEAD
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "r")
        self.file.write("\n\n")
        self.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        self.file.write("\n")
=======
        Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "w")
        Log.file.write("\n\n")
        Log.file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        Log.file.write("\n")
>>>>>>> 4ad29b113cd30ae8e9292f4ae0d6f0dd5c9dd311
        SensorLib.LCD().printData("Log","Open Log File")

    def StopLog(self):
        SensorLib.LCD().printData("Log","Stop Logging")
<<<<<<< HEAD
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        self.file.close()
=======
        #Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        Log.file.close()
>>>>>>> 4ad29b113cd30ae8e9292f4ae0d6f0dd5c9dd311
        
    def LogInfo(self,data):
        # dump output in JSON
        print("Log Info")
        jsonData = json.dumps(str(data))

        # write to file
<<<<<<< HEAD
        self.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        self.file.write("\nRuntime " + str(0) + " :" + str(jsonData) + str("\n") + "dt: " + datetime.today().strftime('%H:%M:%S') +"\n")
=======
        #Log.file = open("/home/pi/Documents/GRN-HSE/log/log.json", "a")
        Log.file.write("\nRuntime " + str(0) + " :" + str(jsonData) + str("\n") + "dt: " + datetime.today().strftime('%H:%M:%S') +"\n")
>>>>>>> 4ad29b113cd30ae8e9292f4ae0d6f0dd5c9dd311


