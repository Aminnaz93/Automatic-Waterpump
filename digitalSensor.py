from machine import Pin
import time

# Anslut sensorns signal till en digital pin (t.ex. Pin 14)
sensor_pin = Pin("D5", Pin.IN)

while True:
    sensor_value = sensor_pin.value()  # Läs av sensorvärdet (HIGH eller LOW)

    if sensor_value == 1:
        print("Jorden är torr")
    else:
        print("Jorden är våt")

    time.sleep(1)  # Vänta en sekund innan nästa mätning