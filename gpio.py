from gpiozero import LED

class GPIO:
    def __init__(self):
        self.rPiFan = LED(24)
        self.humidityFan = LED(23)
        self.tempFan = LED(22)

    # Toggle On/Off RaspberryPi Fan
    def rPiFanAction(self, action):
            if action is True:
                self.rPiFan.on()
            else:
                self.rPiFan.off()

    # Toggle On/Off Humidity Fan
    def humidityFanAction(self, action):
            if action is True:
                self.humidityFan.on()
            else:
                self.humidityFan.off()

    # Toggle On/Off Humidity Fan
    def tempFanAction(self, action):
            if action is True:
                self.tempFan.on()
            else:
                self.tempFan.off()