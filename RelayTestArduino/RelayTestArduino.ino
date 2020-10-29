String incomingByte;
int relayPin = 12;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(relayPin, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readStringUntil('\n');
    if (incomingByte == "on") {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.write("Led on\t");
      digitalWrite(relayPin, HIGH);
      Serial.write("Relay on");
    }
    else if (incomingByte == "off") {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.write("Led off\t");
      digitalWrite(relayPin, LOW);
      Serial.write("Relay off");
    }
    else {
      Serial.write("invald input");
      
    }
  }
}
