---
layout: default
title: "Step 4: Code until now"
parent: "Step 4: Creating a timer"
nav_exclude: true
---

# Step 4: Code until now

```python
##--- Imports
import digitalio
import board
import p9813
import time

##--- Variables
# State variables
state_idle = 0
state_work = 1
current_state = state_idle

# Button variables
buttonpin = board.D7
button = digitalio.DigitalInOut(buttonpin)
button.direction = digitalio.Direction.INPUT

current_button_state = False
last_button_state = False

# For the Chainable LED:
pin_clk = board.D3
pin_data = board.D4
num_leds = 1
leds = p9813.P9813(pin_clk, pin_data, num_leds)

led_off = (0, 0, 0)
led_red = (255, 0, 0)
led_green = (0, 255, 0)
led_blue = (0, 0, 255)  
led_yellow = (255, 255, 0)
led_white = (255, 255, 255)

# Timer variables
work_duration = 5
timer_duration = 0
timer_mark = 0

##--- Functions
##--- Acting Machine cause functions
def check_button_press():
    global current_button_state, last_button_state
    button_press = False
    current_button_state = button.value

    if current_button_state and not last_button_state:
        button_press = True

    last_button_state = current_button_state
    return button_press

def timer_expired():
    global timer_mark, timer_duration
    if time.monotonic() - timer_mark > timer_duration:
        return True
    else:
        return False

##--- Acting machine effect functions
def set_led_color(color):
    global leds
    leds.fill(color)
    leds.write()

def set_timer(duration):
    global timer_duration, timer_mark
    timer_duration = duration
    timer_mark = time.monotonic()

##--- Setup code, code that executes once at start-up

##--- Main loop
while True:
    # State Idle
    if current_state == state_idle:
        if check_button_press():
            print("Switch from Idle to Work") 
            current_state = state_work
            set_led_color(led_green)
            set_timer(work_duration)

    # State Work
    elif current_state == state_work:
        if timer_expired():
            print("Switch from Work to Idle") 
            current_state = state_idle
            set_led_color(led_off)
```

[Return to tutorial](step4){: .btn .btn-blue }