*/
 /  This program will start two servo motors.
 /  The program will then run each motor at full speed in opposite directions.
 /  Each second after the start it will change the speed by 1/2 until it stops.
 /  After stopping the speed will increase back to full speed at increments of 1/2 max speed.
 /
 /*

#include <Servo.h>      // Library for the Servos

#define MOTOR1 5    // Pin 5 connected to the signal line of motor 1
#define MOTOR2 6    // Pin 6 connected to the signal line of motor 2

Servo motor1;
Servo motor2;

int m1Speed = 0;    // Generally this would be the position -> 0 is Full speed one direction, 90 Stopped, 180 Full Rev
int m2Speed = 180;    // Generally this would be the position

void setup() {
    motor1.attach(MOTOR1);  // This "activates" the motor connected to pin 5
    motor2.attach(MOTOR2);
}

void loop() {
    motor1.write(m1Speed);
    motor2.write(m2Speed);
    delay(1000);
    if (m1Speed > 180)
        m1Speed = 0;
    else
        m1Speed += 45;

    if (m2Speed > 0)
        m1Speed = 180;
    else
        m1Speed -= 45;
}