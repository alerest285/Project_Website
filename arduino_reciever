#include <Servo.h>

Servo servo0;
Servo servo1;
Servo servo2;

// create array
int incoming[2];

void setup(){
  Serial.begin(9600);

  servo0.attach(5);
  servo1.attach(3);
  servo2.attach(6);
}

void loop(){
  while(Serial.available() >= 3){
    for (int i = 0; i < 3; i++){
      incoming[i] = Serial.read();
    }
    if (incoming[0] != 255 and incoming[1] != 255 and incoming[2] != 255){
      servo0.write(incoming[0]);
      servo1.write(incoming[1]);
      servo2.write(incoming[2]);
    }
    else
      servo0.write(servo0.read());
      servo1.write(servo1.read());
      servo2.write(servo2.read());
  }
}
