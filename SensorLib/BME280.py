from SensorLib.BME2802 import QwiicBme280
import time
import sys
import json

class BME_280(object):
    bme = None

    def getSensor(self):
        sensor = QwiicBme280()

        if not sensor.connected:
            print("BME280 device NOT Connected")
            sys.exit(0)
            return

        sensor.begin()
        print("BME-280 Is Communicating")
        BME280.bme = sensor
        return BME280.bme

    def getRawData(self):
        bme = BME280.bme
        # Return Better Data (JSON)
        bmeData = {'humidity': bme.humidity, 'pressure': bme.pressure, 'altitude': bme.altitude_meters, 'temperature': bme.temperature_fahrenheit}
        return json.dumps(bmeData)

# if __name__ == '__main__':
# try:
# runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
# print("\nEnding Example 1")
# sys.exit(0)