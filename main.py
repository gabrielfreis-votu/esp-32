from machine import Pin
from time import sleep

verd = Pin(2,Pin.OUT)
ama = Pin(5,Pin.OUT)
verm = Pin(16,Pin.OUT)

while True:
    verm.off()
    verd.on()
    sleep(10)
    verd.off()
    ama.on()
    sleep(4)
    ama.off()
    verm.on()
    sleep(10)
