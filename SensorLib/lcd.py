from __future__ import print_function
import qwiic_serlcd
import time
import sys

class LCD:

    monitor = None
    ifLCD = True

    def getSensor(self):
        myLCD = qwiic_serlcd.QwiicSerlcd()

        if not myLCD.connected:
            ifLCD = False
            return

        myLCD.setBacklight(255, 255, 255)  # Set backlight to bright white
        myLCD.setContrast(5)  # set contrast. Lower to 0 for higher contrast.
        myLCD.clearScreen()  # clear the screen - this moves the cursor to the home position as well

        time.sleep(1)  # give a sec for system messages to complete

        myLCD.print("Hello World!")
        monitor = myLCD

    def printData(self, header, data):
        if LCD.ifLCD is True:
            # do something (print on LCD)
            myLCD.setBacklight(255, 0, 0)  # Set backlight to bright white
            myLCD.setCursor(8, 0)
            myLCD.print(header)
            myLCD.setCursor(0, 1)
            myLCD.print(str(data))
        else:
            # do something else (print on rpi)
            print(header + "\n" + data)

#if __name__ == '__main__':
#    try:
#        runExample()
#    except (KeyboardInterrupt, SystemExit) as exErr:
#       print("\nEnding Example 1")
#       sys.exit(0)
