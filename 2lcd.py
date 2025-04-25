import machine
from machine import Pin, SoftI2C
from time import sleep, ticks_ms
from umqtt.simple import MQTTClient
import network
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

####### Wi-Fi-inställningar #######
ssid = "Tele2_42c7d0"
password = "rgjvdzxq"

####### MQTT-inställningar #######
CLIENT_NAME = "esp32_waterpump10"
BROKER_ADDR = "broker.hivemq.com"
TOPIC = "Waterpump"

####### I2C och LCD-inställningar ########
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = SoftI2C(scl=Pin("A5"), sda=Pin("A4"), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

####### Knapp med interrupt + debounce #######
button_pin = Pin("D4", Pin.IN, Pin.PULL_UP)
last_press_time = 0
debounce_delay = 200  # millisekunder

##### När knappen trycks ned skickas ett MQTT-meddelande ("turn_on") om att starta pumpen #####
##### Debounce används för att förhindra att flera signaler skickas vid ett enda knapptryck #####
def handle_button(pin):
    global last_press_time
    current_time = ticks_ms()
    if current_time - last_press_time > debounce_delay:
        print("Pump on")
        publish_status(b"turn_on")
        last_press_time = current_time

button_pin.irq(trigger=Pin.IRQ_FALLING, handler=handle_button)

###### Anslut till Wi-Fi #######
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        print("Försöker ansluta till Wi-Fi...")
        sleep(1)
        
    print("Ansluten till Wi-Fi!")

###### Skapa MQTT-klient och publicera status #######
mqtt_client = MQTTClient(CLIENT_NAME, BROKER_ADDR)

def publish_status(status):
    mqtt_client.publish(TOPIC, status)
    print(f"Publicerat status: {status}")

###### Callback-funktion för inkommande MQTT-meddelanden #######
# Denna funktion kommer att anropas när ett meddelande tas emot
# och kommer att visa meddelandet på LCD-skärmen.
# Om meddelandet är "turn_on" eller "turn_off" kommer den att styra pumpen
def callback_print(topic, msg):
    print(f"Från topic {topic}: {msg}")
    lcd.clear()
    lcd.putstr(msg.decode())  # Visa meddelande på LCD

###### Initiering och anslutning #######
connect_wifi()
mqtt_client.set_callback(callback_print)
mqtt_client.connect()
mqtt_client.subscribe(TOPIC)
print("Ansluten till MQTT och prenumererar på topic:", TOPIC)
publish_status(b"Ansluten till wifi")
lcd.clear()
lcd.putstr("Vattensystem aktivt")

###### Huvudloop #######
while True:
    mqtt_client.check_msg()  # Tar emot meddelanden till LCD
    sleep(0.1)  # Kort delay för att inte blockera