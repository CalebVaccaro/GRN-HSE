from __future__ import print_function
import qwiic_serlcd
import time
import sys

class LCD:

    monitor = None
    ifLCD = True

    def getSensor():
        myLCD = qwiic_serlcd.QwiicSerlcd()

        if not myLCD.connected:
            LCD.ifLCD = False
            return

        myLCD.setBacklight(255, 255, 255)  # Set backlight to bright white
        myLCD.setContrast(5)  # set contrast. Lower to 0 for higher contrast.
        myLCD.clearScreen()  # clear the screen - this moves the cursor to the home position as well

        time.sleep(1)  # give a sec for system messages to complete

        myLCD.print("Hello World!")
        LCD.monitor = myLCD

    def printData(header, data):
        try:
            if LCD.ifLCD is True:
                # do something (print on LCD)
                LCD.monitor.setBacklight(255, 0, 0)  # Set backlight to bright white
                LCD.monitor.clearScreen()
                LCD.monitor.setCursor(0, 0)
                LCD.monitor.print(header + ":  ")
                LCD.monitor.print(str(data))
                time.sleep(1)
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
