from gpiozero import LED

class GPIO:
    def __init__(self):
        self.rPiFan = LED(27)
        self.humidityFan = LED(23)
        self.tempFan = LED(17)

    # Toggle On/Off RaspberryPi Fan
    def rPiFanAction(self, action):
            if action is True:
                # run Humidity Fan
                self.rPiFan.on()
            else:
                # stop Humidity Fan
                self.rPiFan.off()

    # Toggle On/Off Humidity Fan
    def humidityFanAction(self, action):
            if action is True:
                # run Humidity Fan
                self.humidityFan.on()
            else:
                # stop Humidity Fan
                self.humidityFan.off()

    # Toggle On/Off Humidity Fan
    def tempFanAction(self, action):
            if action is True:
                # run Humidity Fan
                self.tempFan.on()
            else:
                # stop Humidity Fan
                self.tempFan.off()