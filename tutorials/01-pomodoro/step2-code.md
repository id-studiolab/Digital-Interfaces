---
layout: default
title: "Step 2: Code until now"
parent: "Step 2: Setting up the states"
nav_exclude: true
---

# Step 2 Code until now

```python
##--- Imports
import digitalio
import board

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

##--- Setup code, code that executes once at start-up

##--- Main loop
while True:
    # State Idle
    if current_state == state_idle:
        if check_button_press():
            print("Switch from Idle to Work") 
            current_state = state_work

    # State Work
    elif current_state == state_work:
        if check_button_press():
            print("Switch from Work to Idle") 
            current_state = state_idle

```

[Return to tutorial](step2){: .btn .btn-blue }