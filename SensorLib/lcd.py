from __future__ import print_function
import qwiic_serlcd
import time
import sys

class LCD(object):

    monitor = None
    ifLCD = True

    def getSensor(self):
        sensor = qwiic_serlcd.QwiicSerlcd()

        if not sensor.connected:
            LCD.ifLCD = False
            return

        LCD.monitor = sensor
        LCD.monitor.setBacklight(255, 255, 255)  # Set backlight to bright white
        LCD.monitor.setContrast(5)  # set contrast. Lower to 0 for higher contrast.
        LCD.monitor.clearScreen()  # clear the screen - this moves the cursor to the home position as well
        time.sleep(1)  # give a sec for system messages to complete
        
        self.printData("LCD","Display Activated")

    def printData(self,header, data):
        try:
            if LCD.ifLCD is True:
                # do something (print on LCD)
                LCD.monitor.clearScreen()
                LCD.monitor.setCursor(0, 0)
                LCD.monitor.print(header + ":  ")
                LCD.monitor.print(str(data))
            else:
                # do something else (print on rpi)
                print(header + "\n" + data)
        except:
            print("error on LCD")

#if __name__ == '__main__':
#    try:
#        runExample()
#    except (KeyboardInterrupt, SystemExit) as exErr:
#       print("\nEnding Example 1")
#       sys.exit(0)
