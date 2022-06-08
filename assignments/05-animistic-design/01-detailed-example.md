---
layout: default
title: "01: Detailed example of how to control a servo motor with a sequence"
parent: "Week 5+6: Animistic Design"
grand_parent: Assignments
has_children: false
---

# 01: Detailed example of how to control a servo motor with a sequence

In this example we will take a detailed look at what is going on. You will see that the other examples are relatively similar, so they will not need as much explanation.

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

   ```python
   ##--- VarSpeed Variables

   MIN = 0 # The minimum  possible value of our component
   MAX = 180 # The maximum possible value of our component

   vs = Vspeed(init_position=MIN, result="int") # init_position = initial start position // result = float, int
   vs.set_bounds(lower_bound=MIN, upper_bound=MAX) # make the output of the function be within the bounds set
   ```

3. Afterwards we can configure our servo motor by defining the pin we connect it to (Pin `D2`), creating a variable for the motor we can use to steer it, and set an initial angle. If you haven’t worked with a servo before, take a look at its [documentation page](https://id-studiolab.github.io/Connected-Interaction-Kit/components/servo/servo.html).

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

---

Try out the code above yourself, and if you did it successfully, move on to the next example.

[Next Example](02-fading-an-led-pack){: .btn .btn-blue }
