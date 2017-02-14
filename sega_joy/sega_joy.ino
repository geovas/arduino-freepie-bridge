// -------------------------------------------------------

#define SEL 11

#define SN1 A0
#define SN2 A1
#define SN3 A2
#define SN4 A3
#define SN5 12
#define SN6 13

// -------------------------------------------------------

void setup()
{
  pinMode(SEL, OUTPUT);
  digitalWrite(SEL, LOW);
  
  pinMode(SN1, INPUT_PULLUP);
  pinMode(SN2, INPUT_PULLUP);
  pinMode(SN3, INPUT_PULLUP);
  pinMode(SN4, INPUT_PULLUP);
  pinMode(SN5, INPUT_PULLUP);
  pinMode(SN6, INPUT_PULLUP);

  Serial.begin(9600);
}

// -------------------------------------------------------

void loop()
{
  static bool   mode = true;
  unsigned char ans = 0x00;
  
  if (mode)
  {
    mode = false;
    digitalWrite(SEL, HIGH);
    ans |= 0x40;
  }
  else
  {
    mode = true;
    digitalWrite(SEL, LOW);
  }
  delay(10);
  
  if (digitalRead(SN1)) ans |= 0x01;
  if (digitalRead(SN2)) ans |= 0x02;
  if (digitalRead(SN3)) ans |= 0x04;
  if (digitalRead(SN4)) ans |= 0x08;
  if (digitalRead(SN5)) ans |= 0x10;
  if (digitalRead(SN6)) ans |= 0x20;
  Serial.write(ans);
}

// -------------------------------------------------------
