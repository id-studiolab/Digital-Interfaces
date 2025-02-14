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
    if button.value is True: 
        if current_state is state_wait:
            keyboard.press(key)  # Send our defined key as a command...
            print("button is pressed") #Print a confirmation in the serial monitor
            keyboard.release_all()  # and release all keys again
      
            current_state = state_button_is_pressed # Update our state
        
    elif button.value is False:
        if current_state is state_button_is_pressed:
            print("button is released") # Print a confirmation in the serial monitor
            current_state = state_wait # Reset the state
      
    # Sleep for a bit to make the keypress events occur at a human timescale
    # Skilled gamers can do ~7 button presses per second (says ChatGPT)
    time.sleep(0.143)
```