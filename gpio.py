from gpiozero import LED
from time import sleep

rPiFan = LED(23)
humidityFan = LED(27)

sleep(1.5)
rPiFan.on()
humidityFan.on()
sleep(3)
rPiFan.off()
humidityFan.off()