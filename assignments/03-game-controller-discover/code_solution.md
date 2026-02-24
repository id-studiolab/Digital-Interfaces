---
layout: default
title: Code solution
grand_parent: Assignments
parent: "3: Game Controller"
nav_order: 1
has_children: false
---

# Solution

```python
while True:
        if current_state is state_wait:
                if button.value == True:
                        keyboard.press(key)  # Send our defined key as a command...
                        print("button is pressed") #Print a confirmation in the serial monitor
                        current_state = state_button_is_pressed # Update our state
       
        if current_state is state_button_is_pressed:
                if button.value == False:
                        keyboard.release_all()  # and release all keys again
                        print("button is released") # Print a confirmation in the serial monitor
                        current_state = state_wait # Reset the state
 
         # Sleep briefly so keypress events occur at a human timescale.
         # Skilled users can manage ~7 button presses per second, so we
         # sample at roughly twice that rate to satisfy the Nyquist criterion.

    time.sleep(0.07)
```