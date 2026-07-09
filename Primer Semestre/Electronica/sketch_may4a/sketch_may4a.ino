#include <ESP32Servo.h>

#define IN1 26
#define IN2 27
#define IN3 14
#define IN4 12

#define TRIG 5
#define ECHO 18

Servo servo;

long distancia() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);

  long duracion = pulseIn(ECHO, HIGH);
  long distancia = duracion * 0.034 / 2;

  return distancia;
}

void adelante() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void parar() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void izquierda() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
}

void derecha() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
}

void setup() {
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  servo.attach(13);
  servo.write(90); // centro

  Serial.begin(115200);
}

void loop() {
  int d = distancia();
  Serial.println(d);

  if (d > 20) {
    adelante();
  } else {
    parar();
    delay(500);

    // mirar izquierda
    servo.write(150);
    delay(500);
    int izq = distancia();

    // mirar derecha
    servo.write(30);
    delay(500);
    int der = distancia();

    // volver al centro
    servo.write(90);

    if (izq > der) {
      izquierda();
    } else {
      derecha();
    }

    delay(800);
  }
}