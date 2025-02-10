import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

# Initialisera I2C för ESP32
i2c = SoftI2C(scl=Pin("A5"), sda=Pin("A4"), freq=10000) 

# Skapa LCD-objektet med rätt I2C-adress, antal rader och kolumner
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Anslut sensorns signal till en digital pin (t.ex. Pin 14)
sensor_pin = Pin("D5", Pin.IN)

while True:
    sensor_value = sensor_pin.value()  # Läs av sensorvärdet (HIGH eller LOW)

    if sensor_value == 1:
        lcd.clear()  # Rensa LCD-skärmen
        lcd.putstr("Soil is dry")  # Skriv ut på LCD
    else:
        lcd.clear()  # Rensa LCD-skärmen
        lcd.putstr("Soil is wet")  # Skriv ut på LCD

    sleep(0.5)  # Vänta en sekund innan nästa mätning