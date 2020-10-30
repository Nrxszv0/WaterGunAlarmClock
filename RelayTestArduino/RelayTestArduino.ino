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
  //  Serial.println(data);
  //  //data.remove(0, (data.indexOf("Y") + 2));
  //  Serial.println(data);
  //  Serial.println(getCoordX(data));
  //  Serial.println(getCoordY(data));



  delay(100);
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
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
  else if(Serial.available() == 0) {
    serX.write(preSerXVal);
    serY.write(preSerYVal);
  }
  preSerXVal = serXVal;
  preSerYVal = serYVal;


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
