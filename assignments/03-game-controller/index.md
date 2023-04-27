---
layout: default
title: "3: Game Controller"
parent: Assignments
has_children: false
---

# Game Controller
In this weeks assignment we are going to build and embody a physical controller to control a game on our screen.

---

## Download and install needed libraries
For the code to work, we need an additional library that turns our ItsyBitsy into a device that can send keyboard commands to our computer.
1. Download the[ CircuitPython Library Bundle](https://circuitpython.org/libraries) for Version 7.x
2. Search for the folder names `adafruit_hid` and copy it into the `lib` folder of your `CIRCUITPY` device.

---

## Possible games you can play
These are just some examples of games you can play, and there are many more online (or to download). Your chosen embodiment should fit the game!
1. [Flappy Bird](https://flappybird.io)
2. [Drift Boss](https://www.crazygames.com/game/drift-boss?theatreMode=true)
3. [Pong Game](https://www.ponggame.org)
4. [Crazy Flips](https://www.crazygames.com/game/crazy-flips-3d?theatreMode=true)
5. [Canabalt](https://alluracy.itch.io/canabalt-clone)

--- 

## Code examples
You will see that different games need different inputs. Either they expect a single keycode or mouse press, or a continous stream of keycodes to play the game.
---

### Send a single `SPACE` key
```python
##--- Library Imports
import time
import board
import digitalio

# Make sure to download and place the USB HID library in the lib folder of CIRCUITPY
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


##--- Defining states

state_wait = 0
state_button_is_pressed = 1
current_state = 0


##--- Keyboard variables

#We want to emulate a keyboard interface
#To do so we use the usb_hid (Human-interface device) library to send commands to our computer

# Define a new keyboard and set the layout to US (mostly same as the Dutch layout)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# We want to send the SPACE key when the button is pressed
key = Keycode.SPACE


##--- Button variables

## Define a new button variable and assign it to port D13 of our board
button = digitalio.DigitalInOut(board.D13)

## Define the button as an input component
button.direction = digitalio.Direction.INPUT


# Sleep for a bit to avoid a race condition on some systems
time.sleep(1)
print("Waiting for key pin...")

while True:

    if button.value is True and current_state is state_wait:
        keyboard.press(key)  # Send our defined key as a command...
        print("button is pressed") #Print a confirmation in the serial monitor
        keyboard.release_all()  # and release all keys again

        current_state = state_button_is_pressed # Update our state

    if button.value is False and current_state is state_button_is_pressed:
        print("button is released") #Print a confirmation in the serial monitor
        current_state = state_wait #Reset the state

    time.sleep(0.01)
```

---

### Send a continous `SPACE` key
```python
##--- Library Imports
import time
import board
import digitalio

# Make sure to download and place the USB HID library in the lib folder of CIRCUITPY
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode


##--- Defining states

state_wait = 0
state_button_is_pressed = 1
current_state = 0

##--- Keyboard variables

#We want to emulate a keyboard interface
#To do so we use the usb_hid (Human-interface device) library to send commands to our computer

# Define a new keyboard and set the layout to US (mostly same as the Dutch layout)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

# We want to send the SPACE key when the button is pressed
key = Keycode.SPACE

##--- Button variables

## Define a new button variable and assign it to port D13 of our board
button = digitalio.DigitalInOut(board.D13)

## Define the button as an input component
button.direction = digitalio.Direction.INPUT


# Sleep for a bit to avoid a race condition on some systems
time.sleep(1)
print("Waiting for key pin...")

while True:

    if button.value is True and current_state is state_wait:
        keyboard.press(key)  # Send our defined key as a command...
        print("button is pressed") #Print a confirmation in the serial monitor
        current_state = state_button_is_pressed # Update our state
        
    if button.value is False and current_state is state_button_is_pressed:
        print("button is released") #Print a confirmation in the serial monitor
        keyboard.release_all()  # and release all keys again
        current_state = state_wait #Reset the state

    time.sleep(0.01)
```

---

### Send a mouse left click
```python
##--- Library Imports
import time
import board
import digitalio

# Make sure to download and place the USB HID library in the lib folder of CIRCUITPY
import usb_hid
from adafruit_hid.mouse import Mouse


##--- Defining states

state_wait = 0
state_button_is_pressed = 1
current_state = 0

##--- Mouse variables

#We want to emulate a mouse
#To do so we use the usb_hid (Human-interface device) library to send commands to our computer
mouse = Mouse(usb_hid.devices)
mouse_key = Mouse.LEFT_BUTTON

##--- Button variables

## Define a new button variable and assign it to port D13 of our board
button = digitalio.DigitalInOut(board.D13)

## Define the button as an input component
button.direction = digitalio.Direction.INPUT

# Sleep for a bit to avoid a race condition on some systems
time.sleep(1)
print("Waiting for key pin...")

while True:

    if button.value is True and current_state is state_wait:
        mouse.press(mouse_key)  # Send our defined key as a command...
        print("button is pressed") #Print a confirmation in the serial monitor
        current_state = state_button_is_pressed # Update our state
        
    if button.value is False and current_state is state_button_is_pressed:
        print("button is released") #Print a confirmation in the serial monitor
        mouse.release(Mouse.LEFT_BUTTON) # Release the button again
        time.sleep(0.02) # Add a little debounce delay
        current_state = state_wait #Reset the state

    time.sleep(0.01)
```

---

### Control the mouse X axis
```python
##--- Library Imports
import time
import analogio
import board
import digitalio

# Make sure to download and place the USB HID library in the lib folder of CIRCUITPY
import usb_hid
from adafruit_hid.mouse import Mouse


##--- Mouse variables

# We want to emulate a mouse
# To do so we use the usb_hid (Human-interface device) library to send commands to our computer
mouse = Mouse(usb_hid.devices)

##--- Potentiometer variables

# Define a new mouse variable and assign it to port A2 of our board
x_axis = analogio.AnalogIn(board.A2)

# Set variables to control the minimum and maximum of the potentiometer
pot_min = 0.00
pot_max = 3.29
step = (pot_max - pot_min) / 20.0

##--- Helper functions
# Read the pin voltage
def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# Maps the potentiometer voltage range to 0-20
def steps(axis):
    return round((axis - pot_min) / step)

while True:

    x = get_voltage(x_axis)

    if steps(x) > 11.0:
        print(steps(x))
        mouse.move(x=1)
    if steps(x) < 9.0:
        # print(steps(x))
        mouse.move(x=-1)

    if steps(x) > 19.0:
        print(steps(x))
        mouse.move(x=8)
    if steps(x) < 1.0:
        print(steps(x))
        mouse.move(x=-8)
    time.sleep(0.02)  # Debounce delay
```