from SensorLib.BME2802 import QwiicBme280
import time
import sys
import json

class BME_280(object):

    def __init__(self):
        self.bme = None

    def getSensor(self):
        self.bme = QwiicBme280()

        if not self.bme.connected:
            print("BME280 device NOT Connected")
            sys.exit(0)
            return

        self.bme.begin()
        print("BME-280 Is Communicating")
        return self.bme

    def getRawData(self):
        # Return Better Data (JSON)
        bmeData = {
            'humidity': self.bme.humidity,
            'pressure': self.bme.pressure,
            'altitude': self.bme.altitude_meters,
            'temperature': self.bme.temperature_fahrenheit
        }
        return json.dumps(bmeData)

# if __name__ == '__main__':
# try:
# runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
# print("\nEnding Example 1")
# sys.exit(0)