#define TIME_LIMIT 500
#define TIME_STEP 5

int limit_timer = 0;

void setup() {
  pinMode(2, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(10, INPUT);
}

void loop() {
  if (digitalRead(10)) {
    if (limit_timer < TIME_LIMIT) {
      digitalWrite(2, HIGH);
      digitalWrite(13, HIGH);
      limit_timer += TIME_STEP;
    }
    else {
      digitalWrite(2, LOW);
      digitalWrite(13, LOW);
    }
  }
  else {
    digitalWrite(2, LOW);
    digitalWrite(13, LOW);
    limit_timer = 0;
  }
  delay(TIME_STEP);
}
