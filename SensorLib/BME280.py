from SensorLib.BME2802 import QwiicBme280
import time
import sys
import json

class BME_280(object):
    bme = None

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
        bme = self.bme
        # Return Better Data (JSON)
        bmeData = {'humidity': bme.humidity, 'pressure': bme.pressure, 'altitude': bme.altitude_meters, 'temperature': bme.temperature_fahrenheit}
        return json.dumps(bmeData)

# if __name__ == '__main__':
# try:
# runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
# print("\nEnding Example 1")
# sys.exit(0)