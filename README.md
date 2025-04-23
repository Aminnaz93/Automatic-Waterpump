# 🌱 Automatisk Bevattningssystem med ESP32

Detta projekt är ett automatiskt bevattningssystem som använder två ESP32 Nano-enheter för att läsa av jordfuktighet, kolla vattennivå och styra en vattenpump. Systemet kan vattna automatiskt och även manuellt med en knapp. Det visar status på en LCD-display och skickar information via MQTT.

---

## 🧩 Komponenter som används

- 2× ESP32 Nano
- Jordfuktighetssensor
- Vattennivåsensor (kontaktlös)
- Relämodul 5V
- Vattenpump
- LCD-display (I2C, 16x2)
- Tryckknapp (för manuell styrning)
- Plastlådor (för vattenbehållare och komponenter)
- Kablar + breadboard

---

## ⚙️ Funktioner

- Automatisk bevattning om jorden är torr **och** det finns vatten
- Manuell bevattning med knapptryck (`turn_on` via MQTT)
- Visning av systemstatus på LCD
- MQTT-kommunikation med publik broker (Mosquitto)
- Visar felmeddelanden om vatten saknas
- Använder **interrupt och debouncing** för snabbare och stabilare knappstyrning

---

## 🧠 Källkodsbeskrivning

- `2lcd.py`  
  → Styr LCD-displayen, Wi-Fi, MQTT och lyssnar på knapptryck (via interrupt).  
  → Skickar kommandon till den andra ESP32 via MQTT.

- `2pump.py`  
  → Tar emot MQTT-meddelanden, läser av jordfuktighet och vattennivå.  
  → Aktiverar pumpen om villkoren uppfylls.

---

## 📸 Bilder på projektet

| Bild | Beskrivning |
|------|-------------|
| ![Systemöversikt](IMG_8476%20-%20stor.jpg) | Överblick över hela uppkopplingen |
| ![Låda](IMG_8477%20-%20stor.jpg) | Inuti chassit där komponenter är monterade |

---

## 🎥 Video

[▶️ Se videon som visar hur systemet fungerar här](LÄGG-IN-DIN-YOUTUBE-ELLER-DRIVE-LÄNK)

---

## ▶️ Kom igång

1. Ladda upp `2lcd.py` till ena ESP32  
2. Ladda upp `2pump.py` till den andra ESP32  
3. Anslut båda till samma Wi-Fi  
4. Systemet är aktivt! Du kan trycka på knappen eller låta sensorerna sköta vattningen automatiskt.

---

## 💬 MQTT-inställningar

- Broker: `test.mosquitto.org`
- Topic: `Waterpump`
- `turn_on` → Startar pumpen manuellt  
- Status visas på LCD och i terminal

---

## 👨‍🔧 Skapat av

Examensprojekt i mjukvaruutveckling för inbyggda system, 2024–2025.