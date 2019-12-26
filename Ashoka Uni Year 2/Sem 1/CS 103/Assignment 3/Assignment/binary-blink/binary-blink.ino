int val;
const int LED = 13;
int On = HIGH;
int Off = LOW;
int lblink = 3000;
int sblink = 1000;

void setup() {

  // set val (8 bit value)
  val = 69;
  pinMode(LED,OUTPUT);
}

void loop() {
  
  String binval = String(val,BIN);
  int zeros = 8 - binval.length();
  for (int i=0; i<zeros; i++)
  {
    binval = "0" + binval;
  }
  char buff[8];
  binval.toCharArray(buff,8);
  
  for (int i=0; i<8; i++)
  {
    if(buff[i] == '0')
    {
      digitalWrite(LED, On);
      delay(lblink);
      digitalWrite(LED, Off);
    }
    else
    {
      digitalWrite(LED, On);
      delay(sblink);
      digitalWrite(LED, Off);
      delay(100);
      digitalWrite(LED, On);
      delay(sblink);
      digitalWrite(LED, Off);
    }
    delay(500);
  }
  
  // at the beginning of every 10 secs, 
  // blink out the 8 bits of "val" using the built in LED
  // bit 1 - two quick short blinks
  // bit 0 - one long blink
  // gap between bits - 500 ms
    
}

