from __future__ import print_function
import qwiic_serlcd
import time
import sys


class LCD(object):

    def __init__(self):
        self.monitor = None
        self.ifLCD = True

    def getSensor(self):
        self.monitor = qwiic_serlcd.QwiicSerlcd()

        if not self.monitor.connected:
            self.ifLCD = False
            return

        self.monitor.setBacklight(255, 255, 255)  # Set backlight to bright white
        self.monitor.setContrast(5)  # set contrast. Lower to 0 for higher contrast.
        self.monitor.clearScreen()  # clear the screen - this moves the cursor to the home position as well
        time.sleep(1)  # give a sec for system messages to complete

        self.printData("LCD", "Display Activated")

    def printData(self, header, data):
        try:
            if self.ifLCD is True:
                # do something (print on LCD)
                self.monitor.clearScreen()
                self.monitor.setCursor(0, 0)
                self.monitor.print(header + ":  ")
                self.monitor.print(str(data))
            else:
                # do something else (print on rpi)
                print(header + "\n" + data)
        except:
            print("error on LCD")

# if __name__ == '__main__':
#    try:
#        runExample()
#    except (KeyboardInterrupt, SystemExit) as exErr:
#       print("\nEnding Example 1")
#       sys.exit(0)
