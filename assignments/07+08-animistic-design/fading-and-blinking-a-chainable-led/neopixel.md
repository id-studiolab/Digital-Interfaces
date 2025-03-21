---
layout: default
title: "Chainable LED ChaiNEO"
parent: "Fading and blinking a Chainable LED"
grand_parent: "7+8: Animistic Design"
has_children: false
---

# Fading and blinking a Chainable LED

This example used the [Chainable LED](https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/chainable-led-chaineo) of the Connected Interaction Kit, connected to `D13` of the Expander Board.

```python
##--- Library Imports
import time
import board
import neopixel
from varspeed import Vspeed

##--- VarSpeed Variables

MIN = 0.0  # The minimum  possible value of our component
MAX = 1.0  # The maximum possible value of our component

vs = Vspeed(init_position=MIN, result="float")  # init_position = initial start position // result = float, int
vs.set_bounds(lower_bound=MIN, upper_bound=MAX)  # make the output of the function be within the bounds set

##--- Hardware Setup
pin_leds = board.D13
num_leds = 1
leds = neopixel.NeoPixel(pin_leds, num_leds, brightness=0.5, auto_write=False, pixel_order=neopixel.GRBW)

##--- Custom Movement Sequence
# This is where we can define the brightness of our LED
# The sequence will go through each entry and move to the next entry
# The sequence is defined in this format: (next-position,seconds-to-move,number-of-steps,easing function)
# Take a look at different easing functions here: https://easings.net 
led_sequence = [
    (MAX, 0.1, 5, "QuadEaseIn"),
    # Translates to: Go to the MAX value within 0.1 seconds and 5 steps, and use a QuadEaseIn easing function
    (MIN, 1.0, 40, "QuadEaseInOut")
    # Translates to: Go to the MIN value within 1 seconds and 40 steps, and use a QuadEaseInOut easing function
]

# Define what should happen when we get to the end of our sequence
led_looping = 0  # play the sequence in an endless loop forever
# led_looping = 1 # play the sequence only once
# led_looping = 10 # play the sequence 10 times
# led_looping = 15 # play the sequence 15 times

leds.fill((0, 255, 0))  # Color the LED green
leds.show()

##--- Main loop
while True:

    # Make a call to the library and request the desired of our LED
    position, running, changed = vs.sequence(sequence=led_sequence, loop_max=led_looping)

    # See if the values changed for the next move, then do so
    if changed:
        print(
            f'Sequence Num: {vs.seq_pos}, Step: {vs.step}, Position: {position}')

        leds.brightness = position
        leds.show()

```