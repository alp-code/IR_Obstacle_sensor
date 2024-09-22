import RPi.GPIO as gpio
import time

IRpin = 22
LEDpin = 23

def setup():
    gpio.setmode(gpio.BCM) 
    gpio.setup(IRpin, gpio.IN)
    gpio.setup(LEDpin, gpio.OUT)

def loop():
    state = gpio.input(IRpin)
    while True:
        ir_value = gpio.input(IRpin)
        if ir_value == 0 and state == 0:
            gpio.output(LEDpin, gpio.HIGH)
            print('Detektovan Objekat')
            state = 1 
        elif ir_value == 1 and state == 1:
            gpio.output(LEDpin, gpio.LOW)
            print('Bezbedna daljina')
            state = 0
        time.sleep(1)

def destroy():
    gpio.cleanup() 

if __name__ == '__main__':
    try:
        setup()	
        loop()
    except KeyboardInterrupt:
        destroy()