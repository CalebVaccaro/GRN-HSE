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
        while calibrationCounter < 100:
            # set output data
            l.LogInfo(str(o.parseInput(i.getInput())), calibrationCounter, True)
            calibrationCounter += 1

        # Reset Calibration Counter
        calibrationCounter = 0

        # Wait Time for Ranged Values
        while True:
            if runtimeCounter >= 100:
                l.LogInfo(str(o.parseInput(i.getInput())), runtimeCounter, False)
                runtimeCounter = 0
            runtimeCounter += 1

    # Manual ESC
    except (KeyboardInterrupt, SystemExit) as exErr:
        l.StopLog()
        sleep(1)
        sys.exit(0)