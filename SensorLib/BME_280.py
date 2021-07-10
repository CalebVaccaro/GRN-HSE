import qwiic_bme280
import time
import sys
import json

class BME_280:
    bme = None

    def getSensor(self):
        sensor = qwiic_bme280.QwiicBme280()

        if not sensor.connected:
            print("BME280 device NOT Connected", \
                  file=sys.stderr)
            sys.exit(0)
            return

        sensor.begin()
        BME_280.bme = sensor
        print("BME-280 Is Communicating")
        return sensor

    def getRawData(self):
        bme = BME_280.bme
        # Return Better Data (JSON)
        bmeData = {'humidity': bme.humidity, 'pressure': bme.pressure, 'altitude': bme.altitude_meters, 'temperature': bme.temperature_fahrenheit}
        return bmeData

# if __name__ == '__main__':
# try:
# runExample()
# except (KeyboardInterrupt, SystemExit) as exErr:
# print("\nEnding Example 1")
# sys.exit(0)