---
layout: default
title: "02: Fading an LED Pack"
parent: "Week 5: Animistic Design"
grand_parent: Assignments
has_children: false
---

# 02: Fading an LED Pack

This example used the [LED Pack](https://id-studiolab.github.io/Connected-Interaction-Kit/components/led-pack/led-pack.html) of the Connected Interaction Kit, connected to `D2` of the Expander Board.

 

```python
##--- Library Imports
import time
import board
import pwmio
from varspeed import Vspeed

##--- VarSpeed Variables

MIN = 0 # The minimum  possible value of our component
MAX = 65535 # The maximum possible value of our component

vs = Vspeed(init_position=MIN, result="int") # init_position = initial start position // result = float, int
vs.set_bounds(lower_bound=MIN, upper_bound=MAX) # make the output of the function be within the bounds set

##--- Hardware Setup
my_led = pwmio.PWMOut(board.D2, frequency=5000, duty_cycle=0) # create a PWMOut object on Pin D2.
my_led.duty_cycle = MIN # Set the initial LED brightness to 0

##--- Custom Movement Sequence
# This is where we can define the brightness of our LDED
# The sequence will go through each entry and move to the next entry
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net 
led_sequence = [
   (MAX, 5.0, 100, "QuadEaseIn"), # Translates to: Go to the MAX value within 5 seconds and 100 steps, and use a QuadEaseIn easing function
   (MAX, 2.0, 1, "LinearInOut"), # Translates to: Stay on the MAC value for 2 seconds
   (MIN, 5.0, 100, "QuadEaseInOut") # Translates to: Go to the MIN value within 5 seconds and 190 steps, and use a QuadEaseInOut easing function
]

# Define what should happen when we get to the end of our sequence
led_looping = 0 # play the sequence in an endless loop forever
#led_looping = 1 # play the sequence only once
#led_looping = 10 # play the sequence 10 times
#led_looping = 15 # play the sequence 15 times

##--- Main loop
while True:
   
   # Make a call to the library and request the desired of our LED pack
   position, running, changed = vs.sequence(sequence=led_sequence, loop_max=led_looping)
   
   # See if the values changed for the next move, then do so
   if changed:
      print(
         f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')
      my_led.duty_cycle = int(position)
```

[Next Example](03-fading-and-blinking-a-chainable-led){: .btn .btn-blue }
