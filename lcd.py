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

while True:
    # Visa "Hello World!" på LCD:n
    lcd.putstr("Hello World!")
    sleep(2)
    lcd.clear()  # Rensa LCD:n efter 2 sekunder
    sleep(1)

    # Visa en räknare från 0 till 10 på LCD:n
    lcd.putstr("Lets Count 0-10!")
    sleep(2)
    lcd.clear()


    for i in range(11):
        lcd.putstr(str(i))  # Skriv ut räknaren
        sleep(1)
        lcd.clear()  # Rensa LCD:n varje gång