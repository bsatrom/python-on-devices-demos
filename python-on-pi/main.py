import board
import busio
import time
import adafruit_bme680

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

while True:
  temp = sensor.temperature
  humidity = sensor.humidity
  print('Temperature: {} degrees C'.format(temp))
  print('Humidity: {}%'.format(humidity))

  time.sleep(15)