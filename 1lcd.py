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
CLIENT_NAME = "esp32_waterpump10"
BROKER_ADDR = "test.mosquitto.org"  # Använd en korrekt brokeradress här
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
        print("Försöker ansluta till Wi-Fi...")
        sleep(1)
        
    print("Ansluten till Wi-Fi!")
    print("IP-adress:", wlan.ifconfig()[0])  # Skriver ut den tilldelade IP-adressen

# Skapa en funktion för att publicera status via MQTT
def publish_status(status):
    mqtt_client.publish(TOPIC, status)  # Publicera till MQTT-topic
    print(f"Publicerat status: {status}")  # Skriv ut på konsolen

# Skapa MQTT-klient och anslut till broker
mqtt_client = MQTTClient(CLIENT_NAME, BROKER_ADDR)

# Initialisera I2C och LCD
i2c = SoftI2C(scl=Pin("A5"), sda=Pin("A4"), freq=100000)  # Använd GPIO21 (SDA) och GPIO22 (SCL)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)


# Callback-funktion för att ta emot meddelanden via MQTT
def callback_print(topic, msg):
    print(f"Från topic {topic}: {msg}")
    
    # Visa meddelandet på LCD
    lcd.clear()  # Rensa skärmen
    lcd.putstr(msg.decode())  # Visa statusmeddelandet på LCD

# Anslut till Wi-Fi
connect_wifi()

# Skapa MQTT-klient och anslut till broker
mqtt_client.connect()
print("Ansluten till MQTT-broker")

# Publicera status efter anslutning
publish_status("Ansluten till wifi")  # Publicera status när Wi-Fi är anslutet

# Sätt callback-funktion och prenumerera på ämnet
mqtt_client.set_callback(callback_print)
mqtt_client.subscribe(TOPIC)

# Huvudloop för att ta emot meddelanden och visa status på LCD
while True:
    mqtt_client.check_msg()  # Kontrollera om nya meddelanden har tagits emot via MQTT
    sleep(1)  # Vänta en sekund innan nästa kontroll