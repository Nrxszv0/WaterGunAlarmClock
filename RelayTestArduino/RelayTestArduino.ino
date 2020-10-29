#include <Servo.h>
String incomingByte;
int relayPin = 12;
int serXPin = 10, serYPin = 11;
int xVal, yVal;
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

  //  Serial.println(data.remove(data.indexOf("Y",4)));

}

void loop() {
  Serial.println(data);
  //data.remove(0, (data.indexOf("Y") + 2));
//  Serial.println(data);
  Serial.println(getCoordX(data));
   Serial.println(getCoordY(data));
  //  Serial.println(
  //  data.remove(data.indexOf("X"), 2);
  //  data.remove(data.indexOf("Y"));
  //  Serial.println(data);
  while (true) {


  }
  //  delay(10);
  //  if (Serial.available() > 0) {
  //    incomingByte = Serial.readStringUntil('\n');
  //    //    Serial.write(getCoordX(incomingByte));
  //    xVal = getCoordX(incomingByte);
  //    yVal = getCoordY(incomingByte);
  //    Serial.print(xVal);
  //    Serial.print("\t");
  //    Serial.println(yVal);
  //    //      Serial.write(1);
  //  }
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
