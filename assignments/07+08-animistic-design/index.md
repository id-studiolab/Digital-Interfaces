---
layout: default
title: "7+8: Animistic Design"
parent: Assignments
has_children: true
---

# Animistic Design

In the coming two weeks, we are creating an animistic creature – a digital interface that seems alive through different behaviors! 

After exploring non-blocking code in the Party Lamp assignment, we will now apply these concepts to create more complex interactive behaviors. This assignment focuses on creating an object with at least two different (opposing) behavioral states that can be triggered by sensors and expressed through various outputs.

## Assignment Overview

Your task is to design and program an animistic creature that has a distinct personality expressed through at least two opposing behavioral states (e.g., calm/agitated, shy/curious, sleeping/awake). Your prototype should respond to sensor inputs and change its behavior depending on the state it is in.

## The VarSpeed library

Last week we experimented with timers to write non-blocking code. This allowed us to check if a button was being pressed even while fading a led. But using timers is not the only way to achieve this. A different approach involves using the **VarSpeed* library.

Go through the page below to learn what the **VarSpeed** library does and how to use it, then come back to this page once you're done.

[VarSpeed Library Guide](varspeed-library-guide){: .btn .btn-blue }


## Coding assignment

Your assignment is to design your own acting diagram and then implement it in the code.
Here below we provide a code template to help you get started.

## Code Template


{% tabs data-struct %}

{% tab data-struct PicoExpander %}
```python
##--- Main Loop
import board
import neopixel
import digitalio
import time
import pwmio
from varspeed import Vspeed

# -- Define states
# TODO: Change variables according to your behaviours names
state_behaviour_1 = 0   
state_behaviour_2 = 1
#state_behaviour_3 = 2

current_state = state_behaviour_1

# -- Initialize the NeoPixel
led_pin = board.GP10

led = neopixel.NeoPixel(led_pin, 1, brightness=0.5, auto_write=False, pixel_order=neopixel.GRBW)

# Define basic led colors
led_off = (0, 0, 0, 0)
led_red = (255, 0, 0, 0)
led_green = (0, 255, 0, 0)
led_blue = (0, 0, 255, 0)
led_white = (0, 0, 0, 255)

def set_led_color(color):
    global led
    led.fill(color)
    led.show()

##-- VarSpeed Variables

# TODO: Change according to your component
MIN = 0     # The minimum  possible value of our component
MAX = 255   # The maximum possible value of our component

# init_position = initial start position - result = "float", "int"
vs = Vspeed(init_position=MIN, result="int") 

# make the output of the function be within the bounds set
vs.set_bounds(lower_bound=MIN, upper_bound=MAX) 

# TODO: Define your sequence
my_sequence = [

]

# Define how many times the defined sequence should be repeated
looping = 0    # play the sequence in an endless loop forever
#looping = 1   # play the sequence only once
#looping = 10  # play the sequence 10 times

while True:

    # Make a call to the library and request the parameters
    position, running, changed = vs.sequence(sequence=my_sequence, loop_max=looping)

    # - Position: The new value to assign to our servo
    # - Running: False if the sequence is finished, True if it's still running
    # - Changed: False if the value hasn't changed since the last function call, True if it has


    # See if the values changed for the next move, then do so
    if changed:
        print(f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')


    # ----------------------------------------------------------------| 
    #                                                                 | 
    # Use your own Acting Machine Diagram to program your interaction | 
    #                                                                 | 
    # ----------------------------------------------------------------|


    # ----------------------------------------------
    # v DO NOT CHANGE ANYTHING BELOW THIS POINT v  |
    # ----------------------------------------------
    led.show()
    time.sleep(0.1)
   ```
{% endtab %}

{% tab data-struct BitsyExpander %}
```python
##--- Main Loop
import board
import neopixel
import digitalio
import time
import pwmio
from varspeed import Vspeed

# -- Define states
# TODO: Change variables according to your behaviours names
state_behaviour_1 = 0   
state_behaviour_2 = 1
#state_behaviour_3 = 2

current_state = state_behaviour_1

# -- Initialize the NeoPixel
led_pin = board.D13

led = neopixel.NeoPixel(led_pin, 1, brightness=0.5, auto_write=False, pixel_order=neopixel.GRBW)

# Define basic led colors
led_off = (0, 0, 0, 0)
led_red = (255, 0, 0, 0)
led_green = (0, 255, 0, 0)
led_blue = (0, 0, 255, 0)
led_white = (0, 0, 0, 255)

def set_led_color(color):
    global led
    led.fill(color)
    led.show()

##-- VarSpeed Variables

# TODO: Change according to your component
MIN = 0     # The minimum  possible value of our component
MAX = 255   # The maximum possible value of our component

# init_position = initial start position - result = "float", "int"
vs = Vspeed(init_position=MIN, result="int") 

# make the output of the function be within the bounds set
vs.set_bounds(lower_bound=MIN, upper_bound=MAX) 

# TODO: Define your sequence
my_sequence = [

]

# Define how many times the defined sequence should be repeated
looping = 0    # play the sequence in an endless loop forever
#looping = 1   # play the sequence only once
#looping = 10  # play the sequence 10 times

while True:

    # Make a call to the library and request the parameters
    position, running, changed = vs.sequence(sequence=my_sequence, loop_max=looping)

    # - Position: The new value to assign to our servo
    # - Running: False if the sequence is finished, True if it's still running
    # - Changed: False if the value hasn't changed since the last function call, True if it has


    # See if the values changed for the next move, then do so
    if changed:
        print(f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')


    # ----------------------------------------------------------------| 
    #                                                                 | 
    # Use your own Acting Machine Diagram to program your interaction | 
    #                                                                 | 
    # ----------------------------------------------------------------|


    # ----------------------------------------------
    # v DO NOT CHANGE ANYTHING BELOW THIS POINT v  |
    # ----------------------------------------------
    led.show()
    time.sleep(0.1)

    ```
{% endtab %}

{% endtabs %}



## Example Code

Here are some examples to get you started:

[Fading and blinking a Chainable LED](fading-and-blinking-a-chainable-led-index){: .btn .btn-blue }

[Running two sequences](running-two-sequences-index){: .btn .btn-blue }

[Trigger different sequences](trigger-different-sequences-index){: .btn .btn-blue }