import utime
from machine import Pin, I2C

import adafruit_bme680

ledPin = 25

led = Pin(ledPin, Pin.OUT)
i2c = I2C(0)

bmeSensor = adafruit_bme680.BME680_I2C(i2c)
print("Connected to BME680...")

while True:
    # Turn on the LED to take a reading
    led.value(1)

    temp = bmeSensor.temperature
    humidity = bmeSensor.humidity
    print("\nTemperature: %0.1f C" % temp)
    print("Humidity: %0.1f %%" % humidity)

    led.value(0)
    utime.sleep(15)
