void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
float a = analogRead(A0);
float angle = (5-90)/(238-155)*(a*2/2.26-155)+90;
Serial.println(angle);
delay(100);
}
