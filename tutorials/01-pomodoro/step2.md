---
layout: default
title: Step 2 Setting up the states
parent: "01 Pomodoro"
---

# Step 2 Setting up the states
Upon startup, we would like the program to be in an idle state until the user explicitly starts the timer by means of a button press. So, our programming starts with initializing some variables to keep track of the states: state_idle, state_work, and current_state. We represent the different states as integers. The integer stored in current_state can then be compared to the different states to decide what next steps to take. 

```python
##--- Imports

##--- Variables
# State variables
state_idle = 0
state_work = 1
current_state = state_idle

##--- Functions

##--- Setup code, code that executes once at start-up

##--- Main loop
while True:
    # State Idle
    if current_state == state_idle:
        return

    # State Work
    elif current_state == state_work:
        return

```

To switch between the two states, we can add a button to our system. We'll need to import the *digitalio* and *board* libraries to communicate with the button.

```python
##--- Imports
import digitalio
import board

```

Connect the button to pin D7. The following variables allow for communication with the button:

```python
##--- Variables
# Button variables
buttonpin = board.D7
button = digitalio.DigitalInOut(buttonpin)
button.direction = digitalio.Direction.INPUT

```

We will need to create a function that can tell us when the button has been pressed. For this, we need variables that keep track of the current and previous button states. When the last recorded button state is false, and the current button state is true, we know the button has been pressed.

```python
##--- Variables
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

```

Let's alter the main loop in our program to switch between the two states once the button is pressed:

```python
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

It's time to upload your code to the ItsyBitsy and see if it works! Your code should now:

 - Output a print statement once the state changes
 - Switch between states upon button press
 
 Here you can find the code we have until now: ** add link ** 