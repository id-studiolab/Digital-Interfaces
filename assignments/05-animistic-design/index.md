---
layout: default
title: "Week 5+6: Animistic Design"
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

The VarSpeed library solves this issue neatly by allowing us to define actuator behaviour in a simple way. In the code below, we can easily define a sequence of movements for our servo motor (through target-value, time to get to that value, number of steps to get there, and even [easing functions](https://easings.net)) without having to worry about our code being blocked by a `time.sleep()` function. 

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

## Code examples

You will see that all the examples below are mostly the same, and only vary in some small aspect to make them suitable for our intended design. 

It is important to understand that you are **not limited to these examples.** They are here to provide you with a starting point and adapt for your use.