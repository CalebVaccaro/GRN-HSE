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

def timeCounter():
    techCounter = 0
    while techCounter < 50000:
        techCounter += .1

# ** MAIN **
if __name__ == '__main__':

    try:
        # do something
        # get input data
        i.ValidateSensors()
        l.LogLurk()

        # First Time Run
        # run for a min
        while calibrationCounter < 1500:
            # set output data
            o.parseInput(i.getInput())
            timeCounter()
            calibrationCounter += 1

        # Reset Calibration Counter
        calibrationCounter = 0

        # Wait Time for Ranged Values
        while True:
            # Check New Values Every 1 min
            if runtimeCounter >= 25000:
                o.parseInput(i.getInput())
                dataCounter += 1
                runtimeCounter = 0
            timeCounter()
            runtimeCounter += 1

    # Manual ESC
    except (KeyboardInterrupt, SystemExit) as exErr:
        l.StopLog()
        sleep(1)
        sys.exit(0)