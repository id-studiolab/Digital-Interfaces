---
layout: default
title: "Step 3: Adding the LED"
parent: "02 Pomodoro"
grand_parent: "Tutorials"

---

# Step 3: Adding the LED
We can switch between two states, and the program prints some output when this switch happens. It would be nice to have a way to show the user which state the program is in now. We can make use of a LED for this. The ItsyBitsy doesn't have a standard library that can control the Grove Chainable LEDs, so we will need to go through some additional steps for it to work. Follow the tutorial below to get things set up.

[Using a Grove Chainable LED on the ItsyBitsy](https://www.notion.so/Using-a-Grove-Chainable-LED-on-the-ItsyBitsy-96b94be0d93647928cedf38bf2ed4097)

Now we can import the p9813 library, and use it to set up some variables to control the LED.

```python
##--- Imports
import p9813

##--- Variables
# For the Chainable LED:
pin_clk = board.D3
pin_data = board.D4
num_leds = 1
leds = p9813.P9813(pin_clk, pin_data, num_leds)

```

Attach the LED to D3. Let's create a function that can change the LED's color.

```python
##--- Functions
##--- Acting machine effect functions
def set_led_color(color):
    global leds
    leds.fill(color)
    leds.write()

```

The LED takes RGB colors, with each channel ranging between 0 and 255. To make things easier on us, we can store some color variables to use later. 

```python
##--- Variables
led_off = (0, 0, 0)
led_red = (255, 0, 0)
led_green = (0, 255, 0)
led_blue = (0, 0, 255)  
led_yellow = (255, 255, 0)
led_white = (255, 255, 255)

```

Equipped with our new variables and function, we can change the color of the led with only minimal alterations to our original main loop:

```python
##--- Main loop
while True:
    # State Idle
    if current_state == state_idle:
        if check_button_press():
            print("Switch from Idle to Work") 
            current_state = state_work
            set_led_color(led_green)

    # State Work
    elif current_state == state_work:
        if check_button_press():
            print("Switch from Work to Idle") 
            current_state = state_idle
            set_led_color(led_off)
            
```

It's time to upload your code to the ItsyBitsy and see if it works! Your code should now:

 - Output a print statement once the state changes
 - Switch between states upon button press
 - Turn the LED green when the state changes from idle to work
 -  Turn the LED off when the state changes from work to idle
 
[Click here to see the code you should have until now.](step3-code)

[Next Step](step4){: .btn .btn-blue }