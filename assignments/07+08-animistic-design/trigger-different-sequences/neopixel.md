---
layout: default
title: "Chainable LED ChaiNEO"
parent: "Triggering different sequences based on context or interaction"
grand_parent: "7+8: Animistic Design"
has_children: false
---

# Triggering different sequences based on context or interaction

How could we trigger different sequences based on user or context interaction? In this example, we will create a little ItsyCreature that sleeps peacefully until disturbed – in that case it wakes up and gets angry at the disturbance! 

Connect the Chainable LED to pin `D13`, the Servo Motor to pin `D2` and the Touch Sensor to `D3`. By default, the creature will “sleep” in peace, but when touched get angry until the sensor is released again.

---

```python
##--- Library Imports
import time
import board
import neopixel
import pwmio
import digitalio
from adafruit_motor import servo
from varspeed import Vspeed

##--- VarSpeed Variables

MIN_LED = 0  # The minimum  possible value of our component
MAX_LED = 255  # The maximum possible value of our component

vs_led = Vspeed(init_position=MIN_LED, result="int")  # init_position = initial start position // result = float, int
vs_led.set_bounds(lower_bound=MIN_LED, upper_bound=MAX_LED)  # make the output of the function be within the bounds set

MIN_SERVO = 0  # The minimum  possible value of our component
MAX_SERVO = 180  # The maximum possible value of our component

vs_servo = Vspeed(init_position=MIN_SERVO,
                  result="int")  # init_position = initial start position // result = float, int
vs_servo.set_bounds(lower_bound=MIN_SERVO,
                    upper_bound=MAX_SERVO)  # make the output of the function be within the bounds set

##--- Hardware Setup

# Add a touch sensor
touch = digitalio.DigitalInOut(board.D3)
touch.direction = digitalio.Direction.INPUT

pin_leds = board.D13
num_leds = 1
leds = neopixel.NeoPixel(pin_leds, num_leds, auto_write=False, pixel_order=neopixel.GRBW)

pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50)  # create a PWMOut object on Pin D2.
my_servo = servo.Servo(pwm)  # Create a servo object, my_servo
my_servo.angle = MIN_SERVO  # set the servo to a known starting point

##--- Custom Movement Sequence
# This is where we can define the brightness of our LDED
# The sequence will go through each entry and move to the next entry
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net 
led_sequence_sleep = [
    (80, 3, 80, "QuadEaseIn"),
    (80, 2, 1, "LinearInOut"),
    (0, 3, 80, "QuadEaseInOut"),
    (0, 2, 1, "LinearInOut")
]

led_sequence_angry = [
    (MAX_LED, 0.01, 1, "QuadEaseInOut"),
    (MIN_LED, 0.01, 1, "QuadEaseInOut")
]

servo_sequence_sleep = [
    (0, 1.0, 1, "LinearInOut"),
    (10, 0.1, 2, "LinearInOut"),
    (0, 0.1, 2, "LinearInOut"),
    (10, 0.1, 2, "LinearInOut"),
    (0, 0.1, 2, "LinearInOut"),
    (0, 10.0, 11, "LinearInOut")
]

servo_sequence_angry = [
    (10, 0.01, 1, "LinearInOut"),
    (MIN_SERVO, 0.01, 1, "LinearInOut")
]

# Define what should happen when we get to the end of our LED sequence
led_looping = 0  # play the sequence in an endless loop forever
# led_looping = 1 # play the sequence only once
# led_looping = 10 # play the sequence 10 times
# led_looping = 15 # play the sequence 15 times

# Define what should happen when we get to the end of our servo sequence
servo_looping = 0  # play the sequence in an endless loop forever
# servo_looping = 1 # play the sequence only once
# servo_looping = 10 # play the sequence 10 times
# servo_looping = 15 # play the sequence 15 times

# Set the LEDs to off
leds.fill((0, 0, 0))
leds.show()

##--- Main loop
while True:

    if touch.value == False:
        print("sleeping 😴")
        # Make a call to the library and request the desired of our LED
        position_led, running_led, changed_led = vs_led.sequence(sequence=led_sequence_sleep, loop_max=led_looping)

        # See if the values changed for the next move, then do so
        if changed_led:
            # print(f'Sequence Num: {vs_led.seq_pos}, Step: {vs_led.step}, Position: {position_led}')

            # Turn LED White
            led_value = int(position_led)
            leds.fill((0, 0, 0, led_value))
            leds.show()

        # Make a call to the library and request the desired of our servo motor
        position_servo, running_servo, changed_servo = vs_servo.sequence(sequence=servo_sequence_sleep,
                                                                         loop_max=servo_looping)

        # See if the values changed for the next move, then do so
        if changed_servo:
            # print(f'Sequence Num: {vs_servo.seq_pos}, Step: {vs_servo.step}, Position: {position_servo}')
            my_servo.angle = position_servo

    elif touch.value == True:
        print("angry!!! 😡")
        # Make a call to the library and request the desired of our LED
        position_led, running_led, changed_led = vs_led.sequence(sequence=led_sequence_angry, loop_max=led_looping)

        # See if the values changed for the next move, then do so
        if changed_led:
            # print(f'Sequence Num: {vs_led.seq_pos}, Step: {vs_led.step}, Position: {position_led}')

            # Turn LED Red
            led_value = int(position_led)
            leds.fill((led_value, 0, 0))
            leds.show()

        # Make a call to the library and request the desired of our servo motor
        position_servo, running_servo, changed_servo = vs_servo.sequence(sequence=servo_sequence_angry,
                                                                         loop_max=servo_looping)

        # See if the values changed for the next move, then do so
        if changed_servo:
            # print(f'Sequence Num: {vs_servo.seq_pos}, Step: {vs_servo.step}, Position: {position_servo}')
            my_servo.angle = position_servo

    time.sleep(0.05)


```
