#include <Servo.h>
String incomingByte;
int relayPin = 12;
int serXPin = 10, serYPin = 11;
int xVal, yVal;
Servo serX;
Servo serY;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(relayPin, OUTPUT);
  serX.attach(serXPin);
  serY.attach(serYPin);
}

void loop() {
  delay(10);
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    //    Serial.write(getCoordX(incomingByte));
    xVal = getCoordX(incomingByte);
    yVal = getCoordY(incomingByte);
    Serial.print(xVal);
    Serial.print("\t");
    Serial.println(yVal);
    //      Serial.write(1);
  }
}

int getCoordX(String coord) {
  coord.remove(3, 4);
  return coord.toInt();
}
int getCoordY(String coord) {
  coord.remove(0, 4);
  return coord.toInt();
}
