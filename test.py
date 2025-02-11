import machine
from time import sleep

# Sätt reläets styrpinne till en digital pin (t.ex. Pin 12)
relay_pin = machine.Pin("D2", machine.Pin.OUT)

while True:
    relay_pin.on()  # Aktivera reläet (pumpen ska starta)
    sleep(2)
    relay_pin.off()  # Stäng av reläet (pumpen ska stoppas)
    sleep(2)
    