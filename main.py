import sys
from time import sleep
from input import Input
from output import Output
from log import Log

# class easy refs
i = Input
o = Output
l = Log

# counters
calibrationCounter = 0
runtimeCounter = 0

# ** MAIN **
if __name__ == '__main__':
    try:
        # do something
        # get input data
        i.ValidateSensors()
        sleep(.5)
        l.LogLurk()

        # First Time Run
        # run for a min
        while calibrationCounter < 1000:
            # set output data
            l.LogInfo(o.parseInput(i.getInput()), True)
            calibrationCounter += 1

        # Reset Calibration Counter
        calibrationCounter = 0

        # Wait Time for Ranged Values
        while True:
            if runtimeCounter >= 1000000:
                l.LogInfo(o.parseInput(i.getInput()), False)
                runtimeCounter = 0
            runtimeCounter += 1

    # Manual ESC
    except (KeyboardInterrupt, SystemExit) as exErr:
        l.StopLog()
        sleep(1)
        sys.exit(0)