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

#define SOLENOID_DURATION 250

#define GET_BIT(c, bit) (c >> bit & 1)

int solenoid_timer = 0;

char command = 0;
char data = 0;

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

  Serial.print("8bot");
}

void loop() {
  if (Serial.available()) {
    if (command == 0) {
      command = Serial.read();
    }
    else {
      data = Serial.read();

      if (command == 'M') {
        digitalWrite(M1_F, GET_BIT(data, 7));
        digitalWrite(M1_B, GET_BIT(data, 6));
        digitalWrite(M2_F, GET_BIT(data, 5));
        digitalWrite(M2_B, GET_BIT(data, 4));
        digitalWrite(M3_F, GET_BIT(data, 3));
        digitalWrite(M3_B, GET_BIT(data, 2));
        digitalWrite(M4_F, GET_BIT(data, 1));
        digitalWrite(M4_B, GET_BIT(data, 0));
      }
      else if (command == 'A') {
        analogWrite(EN_12, data);
      }
      else if (command == 'B') {
        analogWrite(EN_34, data);
      }
      else if (command == 'S') {
        solenoid_timer = SOLENOID_DURATION;
        digitalWrite(SOLENOID, HIGH);
      }
    }
    command = 0;
  }

  if (solenoid_timer > 0) solenoid_timer--;
  else digitalWrite(SOLENOID, LOW);

  delay(1);
}