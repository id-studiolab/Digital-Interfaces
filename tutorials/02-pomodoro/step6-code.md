---
layout: default
title: "Step 6: Code until now"
parent: "Step 6: Adding the breaks"
nav_exclude: true
---

# Step 6: Code until now

```python
##--- Imports
import digitalio
import board
import p9813
import time
from analogio import AnalogOut

##--- Variables
# State variables
state_idle = 0
state_work = 1
state_break_alarm = 2
state_short_break = 3
state_work_alarm = 4
state_long_break = 5
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
short_break_duration = 3
long_break_duration = 8
timer_duration = 0
timer_mark = 0

break_counter = 0

# Buzzer variables
buzzerpin = board.A0
buzzer = AnalogOut(buzzerpin)

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

def set_buzzer(value):
    if value == True:
        buzzer.value = 65535
    else:
        buzzer.value = 0

##--- Setup code, code that executes once at start-up

##--- Main loop
while True:
    # State Idle
    if current_state == state_idle:
        if check_button_press():
            current_state = state_work
            set_led_color(led_green)
            set_timer(work_duration)
            set_buzzer(False)

    # State Work
    elif current_state == state_work:
        if timer_expired():
            current_state = state_break_alarm
            set_led_color(led_red)
            set_buzzer(True)
    
    # State Break Alarm
    elif current_state == state_break_alarm:
        if check_button_press():
            set_buzzer(False)
            if break_counter < 3:
                current_state = state_short_break
                set_led_color(led_blue)
                set_timer(short_break_duration)
                break_counter = break_counter + 1
            else:
                current_state = state_long_break
                set_led_color(led_white)
                set_timer(long_break_duration)
                break_counter = 0

    # State Short Break
    elif current_state == state_short_break:
        if timer_expired():
            current_state = state_work_alarm
            set_led_color(led_yellow)
            set_buzzer(True)

    # State Long Break
    elif current_state == state_long_break:
        if timer_expired():
            current_state = state_idle
            set_led_color(led_off)
            set_buzzer(False)

    # State Work Alarm
    elif current_state == state_work_alarm:
        if check_button_press():
            current_state = state_work
            set_led_color(led_green)
            set_timer(work_duration)
            set_buzzer(False)
```

[Return to tutorial](step6){: .btn .btn-blue }