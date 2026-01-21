---
layout: default
title: "7+8: Animistic Design"
parent: Assignments
has_children: true
---

# Animistic Design

In the coming two weeks, you will create an **animistic creature** — a digital interface that appears alive through different behaviors.

For this final assignment, it is essential that you understand the difference between **blocking** and **non-blocking** code.

---

## Timing Explained  
### Blocking Code

So far, most of the code you have written has been blocking. Blocking code controls time using:
```python
time.sleep()
```

When ```time.sleep()``` is called, the microcontroller halts execution for the specified number of seconds. During this time:
- No inputs are read
- No outputs are updated
- Nothing else can happen

This approach is fine for simple interactions, such as the Reaction Game. However, it quickly becomes a problem when your system needs to:
- Continuously update LEDs
- Monitor buttons or sensors
- Respond to multiple events at the same time

### Non-blocking code with time.monotonic()

To avoid blocking the program, we can use:
```python
time.monotonic()
```
This function returns the number of **seconds (as a floating-point value)** that have passed since the Python program started running.

Instead of waiting, we:
- Store a time reference
- Continuously check how much time has passed
- Act only when a set interval has expired

This allows the rest of the program to keep running.

---
### Timer functions

The code below provides two helper functions for working with time-based events in a non-blocking way.
Try to understand how it works before using it in your own program.

```python
# -- Import timer library
import time

# -- Timer functions
last_timer_mark = 0
timer_duration = 0

def start_timer(duration):    # Takes duration in seconds
    global last_timer_mark, timer_duration
    last_timer_mark = time.monotonic()
    timer_duration = duration

def is_timer_expired():       # Returns True / False
    return (time.monotonic() - last_timer_mark) > timer_duration
```
**Key idea:**
The program never stops running — it only checks whether enough time has passed.

### Timer examples
```python
import time

start_timer(2.0)             # Creates and starts a timer of 2 seconds 
print(is_timer_expired())    # Will print "False", since 2 seconds haven't passed

time.sleep(3)                # Wait 3 seconds
print(is_timer_expired())    # Will print "True", since more than 2 seconds have passed
```
Once a timer has expired, you can always create a new timer with ```start_timer()``` — this will start a fresh timer with the duration you specify.

### Remember
**Blocking:**  
&nbsp;&nbsp;&nbsp;“Do this, wait, then do the next thing.”  
**Non-blocking:**  
&nbsp;&nbsp;&nbsp;“Keep checking — act when it’s time.”

---
## Assignment goal
In this assignment, you will use non-blocking code to create more complex interactive behaviors.
Your object must have:
- At least two opposing behavioral states (e.g., calm/agitated, shy/curious, sleeping/awake)
- State changes triggered by sensor input (e.g., buttons, sliders, distance, movement)
- Behaviors expressed through outputs (e.g. LEDs, sound, movement)

This approach is essential for creating systems that feel responsive, reactive, and alive.

---

## The VarSpeed library

Last week we experimented with timers to write non-blocking code. This allowed us to check if a button was being pressed even while fading a led. But using timers is not the only way to achieve this. A different approach involves using the **VarSpeed* library.

Go through the page below to learn what the **VarSpeed** library does and how to use it, then come back to this page once you're done.

[VarSpeed Library Guide](varspeed-library-guide){: .btn .btn-blue }


## Coding assignment

Your assignment is to design your own acting diagram and then implement it in the code.
Here below we provide a code template to help you get started.

## Code Template

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
led_pin = board.D10

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

## Example Code

Here are some examples to get you started:

[Fading and blinking a Chainable LED](fading-and-blinking-a-chainable-led-index){: .btn .btn-blue }

[Running two sequences](running-two-sequences-index){: .btn .btn-blue }

[Trigger different sequences](trigger-different-sequences-index){: .btn .btn-blue }