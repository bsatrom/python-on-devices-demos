import board
import time
import adafruit_bme680
import notecard

productUID = "com.blues.brandon.python-temp"

i2c = board.I2C()
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)
card = notecard.OpenI2C(i2c, 0, 0, debug = True)

req = {"req": "hub.set"}
req["product"] = productUID
req["mode"] = "continuous"
rsp = card.Transaction(req)

while True:
  temp = sensor.temperature
  humidity = sensor.humidity
  print('Temperature: {} degrees C'.format(temp))
  print('Humidity: {}%'.format(humidity))

  req = {"req": "note.add"}
  req["file"] = "sensors.qo"
  req["sync"] = True
  req["body"] = { "temp": temp, "humidity": humidity}
  req = card.Transaction(req)
  print(rsp)

  time.sleep(15)