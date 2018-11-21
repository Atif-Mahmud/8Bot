#define EN_12 5
#define M1_F  2
#define M1_B  4
#define M2_F  7
#define M2_B  6

#define EN_34 10
#define M3_F  9
#define M3_B  8
#define M4_F  11
#define M4_B  12

#define SOLENOID  3

void setup() {
  pinMode(EN_12, OUTPUT);
  pinMode(M1_F, OUTPUT);
  pinMode(M1_B, OUTPUT);
  pinMode(M2_F, OUTPUT);
  pinMode(M2_B, OUTPUT);
  pinMode(EN_34, OUTPUT);
  pinMode(M3_F, OUTPUT);
  pinMode(M3_B, OUTPUT);
  pinMode(M4_F, OUTPUT);
  pinMode(M4_B, OUTPUT);
  pinMode(SOLENOID, OUTPUT);

  digitalWrite(EN_12, HIGH);
  digitalWrite(EN_34, HIGH);
}

void loop() {
  digitalWrite(M1_F, HIGH);
  digitalWrite(M2_F, HIGH);
  digitalWrite(M3_F, HIGH);
  digitalWrite(M4_F, HIGH);
  digitalWrite(M1_B, LOW);
  digitalWrite(M2_B, LOW);
  digitalWrite(M3_B, LOW);
  digitalWrite(M4_B, LOW);
  digitalWrite(13, HIGH);

  delay(1000);

  digitalWrite(M1_F, LOW);
  digitalWrite(M2_F, LOW);
  digitalWrite(M3_F, LOW);
  digitalWrite(M4_F, LOW);
  digitalWrite(M1_B, HIGH);
  digitalWrite(M2_B, HIGH);
  digitalWrite(M3_B, HIGH);
  digitalWrite(M4_B, HIGH);
  digitalWrite(13, LOW);

  delay(1000);

  digitalWrite(M1_F, LOW);
  digitalWrite(M2_F, LOW);
  digitalWrite(M3_F, LOW);
  digitalWrite(M4_F, LOW);
  digitalWrite(M1_B, LOW);
  digitalWrite(M2_B, LOW);
  digitalWrite(M3_B, LOW);
  digitalWrite(M4_B, LOW);

  delay(1000);
}