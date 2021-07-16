import sys
from time import sleep
from output import Output
from input import Input
from log import Log

# class easy refs
i = Input()
o = Output()
l = Log()

# counters
calibrationCounter = 0
runtimeCounter = 0
dataCounter = 0

def calCounter():
    techCounter = 0
    while techCounter < 10000:
        techCounter += .1

def runtimeCounter():
    techCounter = 0
    while techCounter < 100000000:
        techCounter += .1

# ** MAIN **
if __name__ == '__main__':

    try:
        # do something
        # get input data
        i.ValidateSensors()
        l.LogLurk()

        while True:
            # --- Full Loop ---
            # First Time Run
            # run for a min
            while calibrationCounter < 1500:
                # set output data
                o.parseQuickPacket(i.getInput(), calibrationCounter)
                calCounter()
                calibrationCounter += 1

            # Reset Calibration Counter
            calibrationCounter = 0

            o.parseInput(i.getInput())

            sleep(20)
            o.clearDataLists()
            # --- End of Loop --- #

    # Manual ESC
    except (KeyboardInterrupt, SystemExit) as exErr:
        l.StopLog()
        sleep(1)
        sys.exit(0)