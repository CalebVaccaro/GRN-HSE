import sys
from time import sleep
from output import Output
from input import Input
from log import Log

# class easy refs
i = Input()
o = Output()
l = Log()


# ** MAIN **
if __name__ == '__main__':

    # counters
    calibrationCounter = 0
    runtimeCounter = 0

    try:
        # do something
        # get input data
        i.ValidateSensors()
        l.LogLurk()

        # First Time Run
        # run for a min
        while calibrationCounter < 151:
            # set output data
            o.parseInput(i.getInput(), calibrationCounter, True)
            print(calibrationCounter)
            calibrationCounter += 1

        # Reset Calibration Counter
        calibrationCounter = 0

        # Wait Time for Ranged Values
        dataCounter = 0
        while True:
            # Check New Values Every 1 min
            if runtimeCounter >= 1000:
                o.parseInput(i.getInput(), dataCounter, False)
                dataCounter += 1
                runtimeCounter = 0
            runtimeCounter += 1

    # Manual ESC
    except (KeyboardInterrupt, SystemExit) as exErr:
        l.StopLog()
        sleep(1)
        sys.exit(0)