"""
The following code engaes two motors attached to pins 5 and 6.

Each motor is
"""

import machine  # https://docs.micropython.org/en/latest/library/machine.html
import utime  # https://docs.micropython.org/en/latest/library/utime.html


class ServoException(Exception):
    pass


class Servo:
    def __init__(self, pin=int(), freq=50, duty_min=40, duty_max=115):
        self.pin = pin
        self.servo = machine.PWM if not pin else machine.PWM(pin, freq)
        self._freq = freq
        self.__duty_min = duty_min
        self.__duty_max = duty_max
        self.duty = int

    def attach(self, pin=int):
        if not pin:
            if self.pin:
                self.servo = machine.PWM(self.pin, self._freq)
            else:
                raise ServoException("No Pin was specified!")
        else:
            self.pin = pin
            self.servo.PWNM(pin, self._freq)

    @staticmethod
    def __map__(value, in_min, in_max, out_min, out_max):
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    def write(self, pos):
        if not pos:
            raise ServoException("Failed to provide a position/speed!")
        if 0 <= pos <= 180:
            val = int(self.__map__(pos, 0, 180, self.__duty_min, self.__duty_max))
            self.servo.duty(val)
            self.duty = pos
        else:
            raise ServoException("Failed to provide a valid position")

    def detach(self):
        self.servo = machine.PWM
        self.pin = int()
        self.duty = int()

    def read(self):
        return self.duty


if __name__ == "__main__":
    motor1 = Servo(5)  # Attach the motor on pin 5 to this object variable
    motor2 = Servo(6)  # Attach the motor on pin 6 to this object variable

    m1Speed = 0  # Gives an initial speed of 100% fwd for motor 1
    m2Speed = 180  # Gives an initial speed of 100% rev for motor 2

    while True:
        motor1.write(m1Speed)  # Writes the speed to the motor
        motor2.write(m2Speed)  # Writes the speed to the motor

        utime.sleep(1)

        if m1Speed < 180:  # Increases the speed until it is 180, 0 is full fwd 90 is stop and 180 is full rev
            m1Speed += 45
        else:
            m1Speed = 0

        if m2Speed > 0:  # Decreases the speed until it is 0, 0 is full fwd 90 is stop and 180 is full rev
            m2Speed -= 45
        else:
            m2Speed = 180
