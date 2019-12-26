void setup() {
  
  pinMode(2, OUTPUT); 
  pinMode(4, OUTPUT); 
  pinMode(7, OUTPUT); 
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
} 

void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float voltage = sensorValue * (5.0 / 1023.0);
  // print out the value you read:
  
  
  if(voltage < 0.1)
  {
    digitalWrite(7, HIGH); 
    digitalWrite(2, LOW);
    digitalWrite(4, LOW);
    tone(9, 261, 1000);
    
  }
  else if(voltage > 1.5)
  {
    digitalWrite(2, HIGH); 
    digitalWrite(7, LOW);
    digitalWrite(4, LOW);
    tone(9, 330, 1000);
  }
  else
  {
    digitalWrite(4, HIGH);
    digitalWrite(2, LOW);
    digitalWrite(7, LOW);
    tone(9, 440, 1000);
  }
  
}
