#include <Wire.h>             // För I2C-kommunikation
#include <LiquidCrystal_I2C.h> // För LCD med I2C

//SDA = A4 SCL = A5 VCC = 5V GND = GND
// Skapa ett LCD-objekt med adress 0x27 och en 16x2 display
LiquidCrystal_I2C lcd(0x27, 16, 2);  

void setup() {
  lcd.begin(16, 2);   // Initiera LCD med 16 kolumner och 2 rader
  lcd.backlight();    // Tänd bakgrundsbelysning på displayen
  
  lcd.setCursor(0, 0); // Placera markören på rad 0, kolumn 0
  lcd.print("carvajal"); // Skriv ut "Hello, World!" på LCD:n
}

void loop() {
  // Inget mer behövs här för detta exempel
}