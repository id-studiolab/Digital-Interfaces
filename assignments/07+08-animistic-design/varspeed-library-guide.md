---
layout: default
title: "VarSpeed Library Guide"
parent: "7+8: Animistic Design"
grand_parent: Assignments
nav_order: 1
---

# VarSpeed Library Guide

## Download and Install

For the code to work, we need an additional library that helps us with controlling different sequences for LEDs, motors, etc.

1. Download the library [here](varspeed.zip)
2. Unzip the library and add the files `varspeed.py` and `easing_functions.py` into the `lib` folder of your `CIRCUITPY`

## Why use the VarSpeed library?

When trying to animate an LED, a servo motor, or any kind of actuator, we have to set its value. This might be the LED color, the motor angle, vibration strength – you name it. 

Usually, we would solve this manually by setting a new value and then a `time.sleep()` like this code that blinks the Chainable LED.

```python
# --- Main loop
while True:
    print("hello world")
    leds.fill((0, 0, 255, 0))
    leds.show()
    time.sleep(2)
    leds.fill((0, 0, 0, 0))
    leds.show()
    time.sleep(2)
```

The issue with this code is that the `time.sleep(2)` function actually *blocks* our entire main loop for two seconds, before continuing. If we want to still read sensors while blinking our LED, or want to move another actuator at a different interval, we run into issues.

The VarSpeed library solves this issue neatly by allowing us to define actuator behaviour in a simple way. In the code below, we can easily define a sequence of movements for our servo motor by providing four inputs:
1. A target-value, 
2. Time to get to that value (in seconds), 
3. Number of steps to get there, 
4. An easing function (see: [easing functions](https://easings.net))

All this without having to worry about our code being blocked by a `time.sleep()` function. 

Take a look at the code examples to get a better understanding of the library and how you can use it to bring your creature to life!

```python
##--- Custom Movement Sequence
# The sequence will go through each entry and move to the next entry
# The sequence is defined with this format: (next-position, seconds-to-move, number-of-steps, easing-function)
# Take a look at different easing functions here: https://easings.net
servo_sequence = [
    (180, 5.0, 100, "LinearInOut"), # Go to value 180, in 5 seconds, in 100 steps, and use a linear easing function.
    (0, 2.0, 5, "QuadEaseOut"),     # Go to value 0, in 2 seconds, in 5 steps, and use a QuadEaseOut easing function
    (90, 2.0, 10, "SineEaseInOut")  # Go to value 90, in 2 seconds, in 10 steps, and use a SineEaseInOut easing function
]
```

## Detailed example with a servo

In this example we will take a detailed look at how to use the VarSpeed library to gradually move a servo. 

1. As always, we start by importing all the libraries we need to run our code.

   ```python
   ##--- Library Imports
   import time
   import board
   import pwmio
   from adafruit_motor import servo
   from varspeed import Vspeed
   ```
   
2. Next, we need to configure the VarSpeed library and define what the minimum and maximum values of our sequence will be as well as pass these values on to the library itself.
For the result we chose `int` because our output should only contain whole numbers.
    
   ```python
   ##--- VarSpeed Variables
   
   MIN = 0 # The minimum possible value of our component
   MAX = 180 # The maximum possible value of our component
   
   vs = Vspeed(init_position=MIN, result="int") # init_position = initial start position // result = float, int
   vs.set_bounds(lower_bound=MIN, upper_bound=MAX) # make the output of the function be within the bounds set
   ```
   
3. Afterwards we can configure our servo motor by defining the pin we connect it to (Pin `D12`), creating a variable for the motor we can use to steer it, and set an initial angle. If you haven't worked with a servo before, take a look at its [documentation page](https://id-studiolab.github.io/Connected-Interaction-Kit/components/servo-motor/servo-motor).


   ```python
   ##--- Hardware Setup
   pwm = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50) # create a PWMOut object on Pin D12.
   my_servo = servo.Servo(pwm) # Create a servo object, my_servo
   my_servo.angle = MIN # set the servo to a known starting point
   ```


   
4. Now instead of having to fiddle with code ourselves to define the motor movement, we can do so by writing it into a sequence that then gets interpreted by the VarSpeed library into the actual angle values.

   You can add as many entries into the `servo_sequence` array as you like, as well as define the `servo_looping` to define how often the sequence should be executed.

   Learn more about different easing functions here: [https://easings.net](https://easings.net/) 

   ```python
   ##--- Custom Movement Sequence
   # This is where we can define the movement of our motor
   # The sequence will go through each entry and move to the next entry
   # The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
   # Take a look at different easing functions here: https://easings.net
   servo_sequence = [
       (180, 5.0, 100, "LinearInOut"), # Go to 180, in 5 seconds, in 100 steps, using a linear function
       (0, 2.0, 5, "QuadEaseOut"),     # Go to 0, in 2 seconds, in 5 steps, using a quadratic easing function
       (90, 2.0, 10, "SineEaseInOut")  # Go to 90, in 2 seconds, in 10 steps, using a sine function
   ]
    
   # Define how many times the defined sequence should be repeated
   #servo_looping = 0   # play the sequence in an endless loop forever
   servo_looping = 1    # play the sequence only once
   #servo_looping = 10  # play the sequence 10 times
   ```
   
5. The last thing to do is to add our main loop, so that the code gets executed continuously.

   ```python
   ##--- Main loop
   while True:
       # Make a call to the library and request the desired position of our servo motor
       position, running, changed = vs.sequence(sequence=servo_sequence, loop_max=servo_looping)

       # - Position: The new value to assign to our servo
       # - Running: False if the sequence is finished, True if it's still running
       # - Changed: False if the value hasn't changed since the last function call, True if it has
   
       # See if the values changed for the next move, then do so
       if changed:
           print(f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')
           my_servo.angle = position
   ```

   Let's have a look at the following statement:

   ```python
   position, running, changed = vs.sequence(sequence=servo_sequence, loop_max=servo_looping)
   ```

   What happens here is that the VarSpeed library contains a function `sequence()` which takes two variables: the desired sequence (`servo_sequence`) and the amount of loops (`servo_looping`). It also returns three variables:
   1. The current position in the sequence (`position`)
   2. Whether the sequence is running (`running`) 
   3. If the value has changed (`changed`)
   
Combined together, the final code for controlling a servo motor with a sequence is this:

```python
##--- Library Imports
import time
import board
import pwmio
from adafruit_motor import servo
from varspeed import Vspeed

##--- VarSpeed Variables

MIN = 0 # The minimum  possible value of our component
MAX = 180 # The maximum possible value of our component

vs = Vspeed(init_position=MIN, result="int") # init_position = initial start position // result = float, int
vs.set_bounds(lower_bound=MIN, upper_bound=MAX) # make the output of the function be within the bounds set

##--- Hardware Setup
pwm = pwmio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50) # create a PWMOut object on Pin D2.
my_servo = servo.Servo(pwm) # Create a servo object, my_servo
my_servo.angle = MIN # set the servo to a known starting point

##--- Custom Movement Sequence
# This is where we can define the movement of our motor
# The sequence will go through each entry and move to the next entry
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
servo_sequence = [
   (180, 5.0, 100, "LinearInOut"), # Go to 180, in 5 seconds, in 100 steps, using a linear function
   (0, 2.0, 5, "QuadEaseOut"),     # Go to 0, in 2 seconds, in 5 steps, using a quadratic easing function
   (90, 2.0, 10, "SineEaseInOut")  # Got to 90, in 2 seconds, in 10 steps, using a sine function
]
    
# Define how many times the defined sequence should be repeated
#servo_looping = 0   # play the sequence in an endless loop forever
servo_looping = 1    # play the sequence only once
#servo_looping = 10  # play the sequence 10 times

while True:
    # Make a call to the library and request the desired of our servo motor
    position, running, changed = vs.sequence(sequence=servo_sequence, loop_max=servo_looping)

    # - Position: The new value to assign to our servo
    # - Running: False if the sequence is finished, True if it's still running
    # - Changed: False if the value hasn't changed since the last function call, True if it has

    # See if the values changed for the next move, then do so
    if changed:
        print(f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')
        my_servo.angle = position

    time.sleep(0.1)
```

[Go back to the assignment](index){: .btn .btn-gray }