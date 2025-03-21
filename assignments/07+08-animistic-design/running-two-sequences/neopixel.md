---
layout: default
title: "Chainable LED ChaiNEO"
parent: "Running two sequences simultaneously"
grand_parent: "7+8: Animistic Design"
has_children: false
---

# Running two sequences simultaneously

When we want to run two sequences at the same time, for example to control a servo and an LED, we basically have to double everything from the individual sequence.

In this example, we will let the [Chainable LED](https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/chainable-led-chaineo) on pin `D13` blink, while we wiggle the servo motor connected to `D2`

```python
##--- Library Imports
import time
import board
import neopixel
import pwmio
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
led_sequence = [
    (MAX_LED, 0.1, 5, "QuadEaseIn"),
    # Translates to: Go to the MAX value within 0.1 seconds and 5 steps, and use a QuadEaseIn easing function
    (MIN_LED, 1.0, 40, "QuadEaseInOut")
    # Translates to: Go to the MIN value within 1 seconds and 40 steps, and use a QuadEaseInOut easing function
]

servo_sequence = [
    (180, 5.0, 100, "LinearInOut"),
    # Translates to: Go to value 180 within 5 seconds and 100 steps, and use a linear easing function
    (0, 2.0, 5, "QuadEaseOut"),
    # Translates to: Go to value 0 within 2 seconds and 5 steps, and use a QuadEaseOut easing function
    (90, 2.0, 10, "SineEaseInOut")
    # Translates to: Go to value 90 within 2 seconds and 10 steps, and use a SineEaseInOut easing function
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

    # Make a call to the library and request the desired of our LED
    position_led, running_led, changed_led = vs_led.sequence(sequence=led_sequence, loop_max=led_looping)

    # See if the values changed for the next move, then do so
    if changed_led:
        print(f'Sequence Num: {vs_led.seq_pos}, Step: {vs_led.step}, Position: {position_led}')

        leds.fill((int(position_led), 0, 0))
        leds.show()

    # Make a call to the library and request the desired of our servo motor
    position_servo, running_servo, changed_servo = vs_servo.sequence(sequence=servo_sequence, loop_max=servo_looping)

    # See if the values changed for the next move, then do so
    if changed_servo:
        print(f'Sequence Num: {vs_servo.seq_pos}, Step: {vs_servo.step}, Position: {position_servo}')
        my_servo.angle = position_servo


```