import machine
from machine import Pin, SoftI2C
from time import sleep
from umqtt.simple import MQTTClient
import network
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

# Wi-Fi inställningar
ssid = "Tele2_42c7d0"
password = "rgjvdzxq"

# MQTT inställningar
CLIENT_NAME = "esp32_waterpump"
BROKER_ADDR = "broker.hivemq.com"
TOPIC = "Waterpump"

# I2C inställningar för LCD
I2C_ADDR = 0x27  # LCD I2C-adress
totalRows = 2
totalColumns = 16

# Anslut till Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        print("Försöker ansluta till wifi...")
        sleep(1)
        
    print("Ansluten till Wifi")
    publish_status("Ansluten till wifi")  # Publicera status när Wi-Fi är anslutet

# Skapa en funktion för att publicera status via MQTT
def publish_status(status):
    mqtt_client.publish(TOPIC, status)  # Publicera till MQTT-topic
    print(f"Publicerat status: {status}")  # Skriv ut på konsolen

# Skapa MQTT-klient och anslut till broker
mqtt_client = MQTTClient(CLIENT_NAME, BROKER_ADDR)
mqtt_client.connect()

# Initialisera I2C och LCD
i2c = SoftI2C(scl=Pin("A5"), sda=Pin("A4"), freq=100000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

# Callback-funktion för att ta emot meddelanden via MQTT
def callback_print(topic, msg):
    print(f"Från topic {topic}: {msg}")
    
    # Visa meddelandet på LCD
    lcd.clear()  # Rensa skärmen
    lcd.putstr(msg.decode())  # Visa statusmeddelandet på LCD

# Sätt callback-funktion och prenumerera på ämnet
mqtt_client.set_callback(callback_print)
mqtt_client.subscribe(TOPIC)

# Anslut till Wi-Fi
connect_wifi()

# Huvudloop för att ta emot meddelanden och visa status på LCD
while True:
    mqtt_client.check_msg()  # Kontrollera om nya meddelanden har tagits emot via MQTT
    sleep(1)  # Vänta en sekund innan nästa kontroll