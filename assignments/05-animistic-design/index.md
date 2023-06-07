---
layout: default
title: "5+6: Animistic Design"
parent: Assignments
has_children: true
---

# Animistic Design

In the coming two weeks we are creating an animistic creature – a digital interface that seems alive! 

---

## Download and install needed libraries

For the code to work, we need an additional library that help us with controlling different sequences for LEDs, motors, etc. You can take a look at the [VarSpeed library documentation here](https://github.com/pvanallen/VarSpeedPython).

1. Download the library [here](varspeed.zip)
2. Unzip the library and add the files `varspeed.py` and `easing_functions.py` into the `lib` folder of your `CIRCUITPY`

---

## Why use the VarSpeed library?

When trying to animate an LED, a servo motor, or any kind of actuator for that matter, we have to set its value. This might be the LED color, the motor angle, vibration strength – you name it. 

Usually, we would perhaps solve this manually by setting a new value and then a `time.sleep()` like this code that blinks the Chainable LED.

```python
# --- Main loop
while True:
    print("hello world")
    leds.fill((0, 0, 255))
    leds.write()
    time.sleep(2)
    leds.fill((0, 0, 0))
    leds.write()
    time.sleep(2)
```

The issue with this code is, that the `time.sleep(2)` function actually *blocks* our entire main loop for two seconds, before continuing. If we want to still read sensors while blinking our LED, or want to move another actuator at a different interval, we run into issues.

The VarSpeed library solves this issue neatly by allowing us to define actuator behaviour in a simple way. In the code below, we can easily define a sequence of movements for our servo motor by providing four inputs:
1. A target-value, 
2. Time to get to that value (in seconds), 
3. Number of steps to get there, 
4. An easing function (see: [easing functions](https://easings.net)))

All this without having to worry about our code being blocked by a `time.sleep()` function. 

Pretty cool! Take a look at the code examples below to get a better understanding of the library and how you can use it to bring your creature to life!

```python
##--- Custom Movement Sequence
# This is where we can define the movement of our motor
# The sequence will go through each entry and move to the next entry
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
servo_sequence = [
    (180, 5.0, 100, "LinearInOut"), # Translates to: Go to value 180 within 5 seconds and 100 steps, and use a linear easing function
    (0, 2.0, 5, "QuadEaseOut"), # Translates to: Go to value 0 within 2 seconds and 5 steps, and use a QuadEaseOut easing function
    (90, 2.0, 10, "SineEaseInOut") # Translates to: Go to value 90 within 2 seconds and 10 steps, and use a SineEaseInOut easing function
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
   
   MIN = 0 # The minimum  possible value of our component
   MAX = 180 # The maximum possible value of our component
   
   vs = Vspeed(init_position=MIN, result="int") # init_position = initial start position // result = float, int
   vs.set_bounds(lower_bound=MIN, upper_bound=MAX) # make the output of the function be within the bounds set
   ```
   
3. Afterwards we can configure our servo motor by defining the pin we connect it to (Pin `D2`), creating a variable for the motor we can use to steer it, and set an initial angle. If you haven’t worked with a servo before, take a look at its [documentation page](https://id-studiolab.github.io/Connected-Interaction-Kit/components/servo-motor/servo-motor).
    
   ```python
   ##--- Hardware Setup
   pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50) # create a PWMOut object on Pin D2.
   my_servo = servo.Servo(pwm) # Create a servo object, my_servo
   my_servo.angle = MIN # set the servo to a known starting point
   ```
   
4. Now the interesting stuff! Instead of having to fiddle with code ourselves to define the motor movement, we can do so by writing it into a sequence that then gets interpreted by the VarSpeed library into the actual angle values.

   You can add as many entries into the `servo_sequence` array as you like, as well as define the `servo_looping` to define how often the sequence should be executed.

   Learn more about different looping functions here: [https://easings.net](https://easings.net/) 

   ```python
   ##--- Custom Movement Sequence
   # This is where we can define the movement of our motor
   # The sequence will go through each entry and move to the next entry
   # The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
   # Take a look at different easing functions here: https://easings.net
   servo_sequence = [
       (180, 5.0, 100, "LinearInOut"), # Translates to: Go to value 180 within 5 seconds and 100 steps, and use a linear easing function
       (0, 2.0, 5, "QuadEaseOut"), # Translates to: Go to value 0 within 2 seconds and 5 steps, and use a QuadEaseOut easing function
       (90, 2.0, 10, "SineEaseInOut") # Translates to: Go to value 90 within 2 seconds and 10 steps, and use a SineEaseInOut easing function
   ]
    
   # Define what should happen when we get to the end of our sequence
   #servo_looping = 0 # play the sequence in an endless loop forever
   servo_looping = 1 # play the sequence only once
   #servo_looping = 10 # play the sequence 10 times
   #servo_looping = 15 # play the sequence 15 times
   ```
   
5. The last thing to do is to add our main loop, so that the code gets executed continuously.

   ```python
   ##--- Main loop
   while True:
       # Make a call to the library and request the desired of our servo motor
       position, running, changed = vs.sequence(sequence=servo_sequence, loop_max=servo_looping)
   
       # See if the values changed for the next move, then do so
       if changed:
           print(
                f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')
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
   
   So basically we say that we have three variables which we want to assign the returned values from the `sequence()` function, therefore we could also write the code as:

   ```python
   data = vs.sequence(sequence=servo_sequence, loop_max=servo_looping)
   position = data[0]
   running = data[1]
   changed = data[2]
   ```

   But this increases the amount of code we have to write and the amount of variables we have to keep track of. 
   
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
pwm = pwmio.PWMOut(board.D2, duty_cycle=2 ** 15, frequency=50) # create a PWMOut object on Pin D2.
my_servo = servo.Servo(pwm) # Create a servo object, my_servo
my_servo.angle = MIN # set the servo to a known starting point

##--- Custom Movement Sequence
# This is where we can define the movement of our motor
# The sequence will go through each entry and move to the next entry
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net
servo_sequence = [
    (180, 5.0, 100, "LinearInOut"), # Translates to: Go to value 180 within 5 seconds and 100 steps, and use a linear easing function
    (0, 2.0, 5, "QuadEaseOut"), # Translates to: Go to value 0 within 2 seconds and 5 steps, and use a QuadEaseOut easing function
    (90, 2.0, 10, "SineEaseInOut") # Translates to: Go to value 90 within 2 seconds and 10 steps, and use a SineEaseInOut easing function
]

# Define what should happen when we get to the end of our sequence
#servo_looping = 0 # play the sequence in an endless loop forever
servo_looping = 1 # play the sequence only once
#servo_looping = 10 # play the sequence 10 times
#servo_looping = 15 # play the sequence 15 times

##--- Main loop
while True:
    
    # Make a call to the library and request the desired of our servo motor
    position, running, changed = vs.sequence(sequence=servo_sequence, loop_max=servo_looping)
    
    # See if the values changed for the next move, then do so
    if changed:
        print(
         f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')
        my_servo.angle = position
```

## More Code examples

You will see that all the examples below are mostly the same, and only vary in some small aspect to make them suitable for our intended design. 

It is important to understand that you are **not limited to these examples.** They are here to provide you with a starting point and adapt for your use.

[Fading and blinking a Chainable LED](03-fading-and-blinking-a-chainable-led-index){: .btn .btn-blue }

[Running two sequences](04-running-two-sequences-index){: .btn .btn-blue }

[Trigger different sequences](05-trigger-different-sequences-index){: .btn .btn-blue }
