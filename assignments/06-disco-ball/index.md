---
layout: default
title: "6: Disco ball"
parent: Assignments
has_children: false
---

# Disco Ball

In this final assignment, we will use the asyncio library in CircuitPython to control an LED disco lamp with multiple modes. The goal is to understand how to manage multiple tasks simultaneously without blocking the execution of the code—something that is crucial when working with animations, sensors, and interactive components.

---

## Prerequisites

For the code to work, we need an additional library that help us with controlling different sequences for LEDs, motors, etc. You can take a look at the [VarSpeed library documentation here](https://github.com/pvanallen/VarSpeedPython).

1. Download the library [here](varspeed.zip)
2. Unzip the library and add the files `varspeed.py` and `easing_functions.py` into the `lib` folder of your `CIRCUITPY`


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
4. An easing function (see: [easing functions](https://easings.net))

All this without having to worry about our code being blocked by a `time.sleep()` function. 

Pretty cool! Take a look at the code examples below to get a better understanding of the library and how you can use it to bring your creature to life!

## Coding instructions


## Coding Assignment
Your goal is to implement a selector that switches between the different modes of the disco ball. 
- 1 potentiomenter
- 1 RGB LED


### Code template

```python
##--- Library Imports
import time
import board
import analogio
import neopixel
from varspeed import Vspeed

##--- Defining states
state_off = 0
state_smooth = 1
state_party = 2

current_state = 0

##--- LED variables
pin_leds = board.D13
num_leds = 1
leds = neopixel.NeoPixel(pin_leds, num_leds, auto_write=False, pixel_order=neopixel.GRBW)

##--- Potentiometer Setup
potentiometer = analogio.AnalogIn(board.A0)

##--- VarSpeed Setup for LED Animation
MIN_BRIGHTNESS = 0   # Minimum brightness level
MAX_BRIGHTNESS = 100 # Maximum brightness level

vs = Vspeed(init_position=MIN_BRIGHTNESS, result="int")
vs.set_bounds(lower_bound=MIN_BRIGHTNESS, upper_bound=MAX_BRIGHTNESS)

##--- Flicker Sequence (Random fast changes)
flicker_sequence = [
   (255, 0.01, 2, "QuadEaseOut"),  
   (50, 0.05, 2, "LinearInOut"),  
   (200, 0.03, 1, "SineEaseInOut"),  
   (0, 0.05, 2, "LinearInOut"),    
]

##--- Smooth Dimming Sequence
smooth_sequence = [
   (100, 0.8, 20, "SineEaseInOut"),  # Brighten smoothly
   (0, 0.8, 20, "SineEaseInOut"),  # Dim smoothly
]

##--- Main Loop

while True:

    brightness, running, changed = vs.sequence(sequence=[], loop_max=1)

    # -------------------------------------------------------------| 
    #                                                              | 
    # Use the Acting Machine Diagram to program your solution here | 
    #                                                              | 
    # -------------------------------------------------------------|

    time.sleep(0.1)

```


## Extra challenge

TODO: Design your own light effect...