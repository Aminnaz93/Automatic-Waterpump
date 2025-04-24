# 🌱 Automatisk Bevattningssystem med ESP32

Detta projekt är ett automatiskt bevattningssystem som använder två ESP32 Nano-enheter för att läsa av jordfuktighet, kontrollera vattennivå och styra en vattenpump. Systemet kan vattna automatiskt eller manuellt via en knapp. Det visar status på en LCD-display och skickar meddelanden via MQTT.

---

## 🧩 Komponenter

- 2× ESP32 Nano
- Jordfuktighetssensor
- Vattennivåsensor (kontaktlös)
- Relämodul 5V
- Vattenpump
- LCD-display (I2C, 16x2)
- Knapp för manuell vattning
- Plastlådor (för vatten och komponenter)
- Breadboard + kopplingskablar

---

## ⚙️ Funktioner

- Automatisk vattning när jorden är torr och vatten finns
- Manuell styrning via knapp (genom MQTT)
- Visar status på LCD (fuktstatus, vattentillgång, pumpstatus)
- Skickar data till MQTT-broker
- Reagerar snabbt med interrupt + debouncing för knappen

---

## 📄 Källkodsöversikt

- `2lcd.py`:  
  Sköter LCD, MQTT-sändning och knapptryck (med interrupt).  
- `2pump.py`:  
  Läser sensorer, styr relä och publicerar systemstatus.

---

## 📸 Bilder

| Bild | Beskrivning |
|------|-------------|
| ![LCD och knapp på breadboard](IMG_8478%20-%20stor.jpeg) | ESP32 med LCD-display och grön knapp på breadboard. Visar meddelande från systemet. |
| ![Komponentlåda med ESP32 och relä](IMG_8480%20-%20stor.jpeg) | Inuti plastlådan: ESP32 kopplat till komponenternadas, snyggt organiserat på breadboard. |
| ![Vattenbehållare med pump](IMG_8481%20-%20stor.jpeg) | Vätskenivåsensor fastklistrad utanför behållaren. |

---

## ▶️ Användning

1. Ladda upp `2lcd.py` till första ESP32 (styrning)
2. Ladda upp `2pump.py` till andra ESP32 (vattenkontroll)
3. Anslut båda till Wi-Fi (ändra `ssid` och `password` i koden)
4. Systemet startar och är redo att användas direkt

---

## 💬 MQTT-konfiguration

- Broker: `test.mosquitto.org`
- Topic: `Waterpump`
- Skicka `turn_on` → Startar pumpen manuellt
- Alla statusmeddelanden visas på LCD och skickas till MQTT

---

## 📁 Bilagor

- `2lcd.py`  
- `2pump.py`  
- Bilder från projektet
- Eventuell video

---

## 👨‍🔧 Skapat av

Examensarbete inom Mjukvaruutveckling för inbyggda system, 2024–2025.