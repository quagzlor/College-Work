float env1;
float env2;
float time_start;
float time_end;
int flag=1;

void setup() {

  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  
  int sensorValue = analogRead(A0);
  
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  env1 = sensorValue+20;
  Serial.print(env1);

  sensorValue = analogRead(A1);

  env2 = sensorValue+20;
  Serial.print(env2);
  
} 

void loop() {
 
  // read the input on analog pinss
  int sensorValue1 = analogRead(A0);
  int sensorValue2 = analogRead(A1);
  
  // Convert the analog reading (which goes from 0  1023) to a voltage (0 - 5V):
  float distance = 0.15;
  float current_vol1 = sensorValue1;
  float current_vol2 = sensorValue2;

  if(current_vol1 > env1)
  {
    time_start = millis();
  }

  if(current_vol2 > env2)
  {
    if(flag==1)
    {
      time_end = millis();
  
      float time_taken = (time_end - time_start)*0.001;
      Serial.println("Time:");
      Serial.println(time_taken);
      float speed_s = distance/time_taken;
      Serial.println("Speed:");
      Serial.println(speed_s);

      flag=0;
    }
  }
}
