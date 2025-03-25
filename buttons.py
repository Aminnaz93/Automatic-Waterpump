import machine
from machine import Pin
from time import sleep

# Definiera knappen på digital pin D4
button_pin = Pin("D4", Pin.IN, Pin.PULL_UP)  # Använd intern pull-up motstånd

# Huvudloop för att läsa knappens tillstånd
while True:
    if not button_pin.value():  # Om knappen är nedtryckt (PULL_UP: LOW när nedtryckt)
        print("Knappen är nedtryckt!")
    else:
        print("Knappen inte tryckt.")
    
    sleep(1)  # Vänta en sekund innan nästa kontroll