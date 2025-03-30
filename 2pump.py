#2pump.py
import machine
from machine import Pin
from time import sleep
from umqtt.simple import MQTTClient
import network

# Wi-Fi inställningar
ssid = "Tele2_42c7d0"
password = "rgjvdzxq"

# MQTT inställningar
CLIENT_NAME = "esp32_waterpump"
BROKER_ADDR = "test.mosquitto.org"
TOPIC = "Waterpump"  # Ämnet du använder för att publicera och prenumerera

# Anslut till Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)  # Aktivera Wi-Fi
    wlan.connect(ssid, password)
    
    while not wlan.isconnected():
        print("Försöker ansluta till Wi-Fi...")
        sleep(1)
        
    print("Ansluten till Wi-Fi!")

connect_wifi()

# Skapa MQTT-klient och anslut till broker
mqtt_client = MQTTClient(CLIENT_NAME, BROKER_ADDR)
mqtt_client.connect()

# Anslut sensorns signaler till digitala pinnar
MoistureSensor_pin = Pin("D5", Pin.IN)  # Jordfuktighetssensor
WaterLevelSensor_pin = Pin("D6", Pin.IN)  # Vätskenivåsensor

# Anslut reläets styrpinne till en digital pin (t.ex. Pin 12)
relay_pin = Pin("D12", machine.Pin.OUT)

# Funktion för att publicera status (pump på/av)
def publish_status(status):
    mqtt_client.publish(TOPIC, status)
    print(f"Publicerat status: {status}")  # Skriv ut på konsolen

# Callback-funktion för att ta emot meddelanden via MQTT
def callback_print(topic, msg):
    print(f"Från topic {topic}: {msg}")
    if msg == b"turn_on":
        
        relay_pin.on()  # Slå på pumpen
        publish_status("Pump on")  # Publicera status
    elif msg == b"turn_off":
        relay_pin.off()  # Stäng av pumpen
        publish_status("Pump off")  # Publicera status

# Sätt callback-funktion och prenumerera på ett ämne
mqtt_client.set_callback(callback_print)
mqtt_client.subscribe(TOPIC)

while True:
    moisture_value = MoistureSensor_pin.value()  # Läs av sensorvärdet för jordfuktighet
    water_level_value = WaterLevelSensor_pin.value()  # Läs av sensorvärdet för vätskenivå
    
    # Kontrollera om både jorden är torr och det finns vätska i flaskan
    if moisture_value == 1 and water_level_value == 1:
        # Jorden är torr, och vätska detekteras, slå på pumpen
        relay_pin.on()  # Slå på reläet (pumpen startar)
        publish_status("Soil is dry, watering")  # Publicera till MQTT
    elif water_level_value == 0:
        # Ingen vätska detekteras, publicera meddelande och stäng av pumpen
        relay_pin.off()  # Stäng av reläet (pumpen stoppas)
        publish_status("No water detected")
    else:
        # Antingen jorden är våt eller ingen vätska detekteras, stäng av pumpen
        relay_pin.off()  # Stäng av reläet (pumpen stoppas)
        publish_status("Soil is wet, no watering")

    mqtt_client.check_msg()  # Kontrollera om nya meddelanden har tagits emot via MQTT
    sleep(1)  # Vänta en sekund innan nästa mätning