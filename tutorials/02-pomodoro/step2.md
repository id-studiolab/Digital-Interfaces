---
layout: default
title: "Step 2: Setting up the states"
parent: "02 Pomodoro"
grand_parent: "Tutorials"
---

# Step 2.A: Setting up the states
Upon startup, we would like the program to be in an idle state until the user explicitly starts the timer by means of a button press.
To do so we will start with implementing two things:
1. Variables and logic to handle the different states.
2. A button to toggle between states. 

First we need to define three variables: `state_idle`, `state_work`, and `current_state`. We represent the different states as integers. We can add these variables under the `##—-Variables` paragraph:

```python
##--- Variables
# State variables
state_idle = 0
state_work = 1
current_state = state_idle
```

The integer stored in `current_state` can then be compared to the different states to decide what next steps to take inside the `##—- Main loop`:

```python
##--- Main loop
while True:
    # State Idle
    if current_state == state_idle:
        return

    # State Work
    elif current_state == state_work:
        return

```

# Step 2.B: Implementing a button
To switch between the two states, we can add a button to our system. We'll need to import the *digitalio* and *board* libraries to communicate with the button.

```python
##--- Imports
import digitalio
import board

```

Connect the button to pin `D7`. The following variables allow for communication with the button:

```python
##--- Variables
#...
# Button variables
buttonpin = board.D7
button = digitalio.DigitalInOut(buttonpin)
button.direction = digitalio.Direction.INPUT

```

We will need to create a function that can tell us when the button has been pressed. For this, we need two variables that keep track of the current and previous button states. To do this we can add two new variables in our `##—- Variables` paragraph:

```python
##--- Variables
#...
current_button_state = False
last_button_state = False

```

When the last recorded button state is false, and the current button state is true, we know the button has been pressed. To use these states we create a function to check if the button is being pressed in the `##—- Functions` Paragraph:

```python
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
 
[Click here to see the code you should have until now.](step2-code)

[Next Step](step3){: .btn .btn-blue }
