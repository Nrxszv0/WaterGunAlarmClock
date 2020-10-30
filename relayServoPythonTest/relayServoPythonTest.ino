#include <Servo.h>
String incomingByte;
int relayPin = 12;
int serXPin = 7, serYPin = 8;
int serXVal = 0, serYVal = 0;
int xVal, yVal;
int preSerXVal, preSerYVal;
Servo serX;
Servo serY;
String data = "X:60Y:30", fData;

boolean pRun = false;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(relayPin, OUTPUT);
  serX.attach(serXPin);
  serY.attach(serYPin);
  serX.write(90);
  serY.write(90);

}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    if (incomingByte == "on") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write("Led on\t");
      digitalWrite(relayPin, HIGH);
      Serial.write("Relay on");
      pRun = true;
    }

    while (pRun) {
      delay(100);
      if (Serial.available() > 0) {
        incomingByte = Serial.readStringUntil('\n');
        if (incomingByte == "off") {
          digitalWrite(LED_BUILTIN, LOW);
          Serial.write("Led off\t");
          digitalWrite(relayPin, LOW);
          Serial.write("Relay off");
          pRun = false;
          break;
        }
        //    Serial.write(getCoordX(incomingByte));
        xVal = getCoordX(incomingByte);
        yVal = getCoordY(incomingByte);
        Serial.print(xVal);
        Serial.print("\t");
        Serial.print(yVal);
        serXVal = map(xVal, 0, 640, 160, 0);
        serYVal = map(yVal, 0, 360, 160, 0);
        Serial.print("\t");
        Serial.print(serXVal);
        Serial.print("\t");
        Serial.println(serYVal);
        serX.write(serXVal);
        serY.write(serYVal);
      }
      else if (Serial.available() == 0) {
        serX.write(preSerXVal);
        serY.write(preSerYVal);
      }
      preSerXVal = serXVal;
      preSerYVal = serYVal;
    }
    digitalWrite(LED_BUILTIN, LOW);
    Serial.write("Led off\t");
    digitalWrite(relayPin, LOW);
    Serial.write("Relay off");
  }
}
int getCoordX(String coord) {
  coord.remove(coord.indexOf("X"), 2);//removes X:
  coord.remove(coord.indexOf("Y")); //removes Y to end
  return coord.toInt();
}
int getCoordY(String coord) {
  coord.remove(0, (coord.indexOf("Y") + 2));//removes X to Y:
  return coord.toInt();
}
