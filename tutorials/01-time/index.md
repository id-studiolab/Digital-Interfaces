---
layout: default
title: "01 Time in CircuitPython"
has_children: false
parent: "Tutorials"
---

# Dealing with Time in Circuit Python - Coding Seminar

# **Modules and Libraries in Circuit Python**

*****************For more information on Modules and Libraries also see the [FAQ section](https://www.notion.so/FAQ-4d1e68a1814b4fd890f08981efcf8a1b) on this page.*

- Modules and libraries are handled quite similarly in many ways. A library will often (maybe always?) be a collection of modules.
- Some **Libraries** also come bundled with the (Circuit)Python installation, and you can see what's on your ItsyBitsy by exploring the file structure.
- If you need to add a **Library** that you don't already have, it's a fairly simple case of downloading it and then copying it to the correct place in the ItsyBitsy file structure. Check the **reference documentation** if you need more help on doing this.
- In order to **use** a **Module** (even a Core Module) or a **Library** that has been installed on your device, you still need to "add it" in each session. This can be done in the (Circuit)Python Console, if you're working there, or in the .py file if you're writing one. This is done using the **import** command. (See example below)
    
    ```jsx
    import time
    ```
    

## The Import Command

*****************For more information on Modules and Libraries also see the [FAQ section](https://www.notion.so/FAQ-4d1e68a1814b4fd890f08981efcf8a1b) on this page.*

- The basic way of doing this is to simply write "**import module_name**" or "**import library_name**" (note that you do this with no file extension, so no ".py" on the name)
- Some modules have pretty long names, and generally in order to use any of the functionality you have to type the name (among other things...). For this reason, there's an option to "**import long_module_name as short_name**" or "**import long_library_name as short_name**".
    
    So instead of:
    
    ```jsx
    import digitalio
    
    button = digitalio.DigitalInOut(board.D13)
    ```
    
    You can write:
    
    ```python
    import digitalio as dig
    
    #Now you can refer to ‘digitalio’ with just ‘dig’
    button = dig.DigitalInOut(board.D13)
    ```
    
- There is also the option to import only certain functions, constants etc. from a module or library. This is done using the "**from module import function"** syntax e.g. "**from math import sin**". One of the main benefits of doing this is also short-hand. If you import the whole math module, then to use sin you have to write "**math.sin(something)**". If you use the "from" approach above, then you can just do "**sin(something)**"
    
    ```jsx
    import usb_hid
    from adafruit_hid.keyboard import Keyboard
    ```
    

## **Finding out what’s in a Module or Library**

*****************For more information on Modules and Libraries also see the FAQ section on this page.*****************

- While you would often want to check documentation online, it can sometimes be quite useful to interrogate the functionality offered by a module or library from within (Circuit)Python.
- This can be done from the (Circuit)Python console. First you import the thing you want to use e.g. "**import math**", then you have two options:
    - Typing "**dir(math)**" will simply give you a list of the functions and values 'inside' it
    - Typing "**help(math)**" will give you a much longer answer, that actually describes all the functions and values and what they do.
    - As a compromise, you also have the option to see the list of things using "**dir()**", and then find out a bit more about it by using "help()". For example, you could write "**help(math.sin)**" to find out about the sin function specifically.

# **Time in Circuit Python**

You often need to take time into account one way or another when writing programs. The **Core Module** called **time** can help us with this! It has a few more bits of functionality than I will describe here (check the documentation if you're interested). I will focus on the most important and fundamental functions, which are also very useful for the type of thing's you might be doing.

**time.sleep(seconds_as_floating_point)** **[returns nothing]**

This function is very easy to use and is sometimes the right approach - but often it's not!

- This makes the processor (and hence the program) stop at that line and wait for the specified amount of time.
- This is a simple way to introduce a delay of known duration between two steps.
- Think of it like the count-down timer on your phone. When the code gets to that line, it set's a timer for the specified time, then goes to sleep until the timer ‘beeps’, it which point it wakes up and keeps going.
- The problem is that the processor can't do anything else (with a few exceptions, e.g. it will still detect and count pulses using **countio**) during this time. So it's a waste of processor power, and prevents the program from responding to anything else during that time.
- For a sufficiently simple program the waste of time might not be an issue, and in some circumstances it's ok that the system becomes unresponsive for a short while, so it *can* be a valid solution in some cases, particularly where very short delays are used.

**time.monotonic()** **[returns time_in_seconds_as_floating_point]** or the 
**time.monotonic_ns() [returns time_in_nanosecons_as_long_integer]**

are often a better way of doing time related stuff. But it takes a little bit more thought and coding to make use of them.

Calling either of these functions can be thought of as consulting a stop-watch that is always running and counting up. The actual value is meaningless because the starting point is arbitrary, but that doesn't matter if you look at the difference between two readings taken at different times.

Difference between **time.monotonic()** and **time.monotonic_ns()**

 is just down to how time is represented:

- With **"time.monotonic()**" you get a **floating point** number that represents time in **seconds**. Having the number in seconds is often convenient, because it's a fairly intuitive measure of time.
- Due to the way floating point numbers are represented: an arbitrarily large number can be represented; but the precision that can be represented decreases as the number gets bigger. Initially you get precision of 1ms or better, but after an hour and a bit that will start decreasing (first to 2ms, then 4ms and so on).
- So, if you need sub-millisecond precision, or if you need millisecond precision over fairly long periods, this is not the one to use.
- With "**time.monotonic_ns()**" you get an **integer** that represents the time in **nanoseconds** (1 second = 1,000,000,000 nanoseconds = 1e9 nanoseconds). This is obviously a less intuitive measure of time.
- Due to the way integers are handled by Python (this is **not** the case in many other languages like C++), there is no specific limit to the size of number that can be represented. As the number gets bigger, more and more memory will be allocated to represent it. Of course, *eventually* the board will run out of memory, but that would take quite an extreme situation.
- So, using this approach will give you much finer time resolution that never deteriorates, but at the expense of more memory and, possibly, a slightly higher CPU load for doing the necessary sums.
- Also note: even though it represents time in nanoseconds, don't expect to be able to use resolution that fine. The CPU is only 120MHz, so each CPU clock cycle is going to take around 10ns, and most Python commands are going to take multiple clock cycles to complete. So probably stick to microseconds or longer!

**Illustrative Examples Involving Time**

To illustrate these concepts, we will consider two examples: blinking an LED, and detecting a "double click" of a button. The associated programs are provided.

Example 1: Blinked an LED

Two programs are provided, both of which make the on-board LED blink at 1Hz and 50% duty cycle (i.e. on for 500ms, off for 500ms and so on).

Program 1: using **time.sleep()**

The first program (“LED blink using sleep.py”) does this using **time.sleep()**: it turns on the LED, sleeps for 500ms, turns off the LED, sleeps for 500ms and repeats. (See the detailed comments in the code for further explanation)

- This works totally fine if you just want to make one LED blink (how exciting!).
- But what if you had two LEDs that you wanted to blink at different frequencies? Or what if you simply wanted the microcontroller to do something else while the LED was blinking?
- In this case, both of those things would be impossible. The processor spends 99,9999...% of its time sleeping!

```python
# Import the required libraries:
#   - board: Provides pin definitions specific to the board being used.
#   - digitalio: Provides digital input/output functionality.
#   - time: Provides time-related functions, such as sleep().
import board
import digitalio
import time

# Create a DigitalInOut object for the onboard LED, which is connected to pin D13.
led = digitalio.DigitalInOut(board.D13)

# Set the direction of the 'led' object as OUTPUT, allowing us to control the LED state.
led.direction = digitalio.Direction.OUTPUT

# Start an infinite loop to repeatedly execute the code within.
while True:
    # Set the LED value to True, which turns it ON.
    led.value = True

    # Pause the program execution for 0.5 seconds (500 milliseconds) while the LED remains ON.
    time.sleep(0.5)

    # Set the LED value to False, which turns it OFF.
    led.value = False

    # Pause the program execution for 0.5 seconds (500 milliseconds) while the LED remains OFF.
    time.sleep(0.5)

    # The loop will repeat, causing the LED to blink on and off every half second.
```

Program 2: using **time.monotonic()**

The second program (“LED blink using time monotonic.py”) achieves the same thing using **time.monotonic()**: it notes the last time it changed the LED state, keeps looping and checking the time, and changes the state again when enough time has passed (See the detailed comments in the code for further explanation)

- The resulting LED behaviour is identical to the previous example.
- In this very simple case, the processor spends 99.999...% of its time checking the 'stopwatch' and calculating whether enough time has passed.
- *However*, the key difference is that you could add much more code inside the **while** loop, and it would do that between 'stopwatch checks'. As long as that code takes much less than 500ms to execute (which would almost always be the case - it's pretty hard to keep a microcontroller busy for 500ms without telling it to wait!), then the blinking would continue.
- See the third program (“LED blink using time monotonic multiple LEDs.py”) for an example where the program is extended to blink two LEDs at different frequencies, assuming one is connected to D1 and the other to D2.

```python
# Import the required libraries:
#   - board: Provides pin definitions specific to the board being used.
#   - digitalio: Provides digital input/output functionality.
#   - time: Provides time-related functions, such as monotonic() and sleep().
import board
import digitalio
import time

# Create a DigitalInOut object for the onboard LED, which is connected to pin D13.
led = digitalio.DigitalInOut(board.D13)

# Set the direction of the 'led' object as OUTPUT, allowing us to control the LED state.
led.direction = digitalio.Direction.OUTPUT

# Set the blink rate for the LED (in seconds). In this case, 0.5 seconds.
blinkRateLED = 0.5

# Initialize the LED state to False (off).
led.value = False

# Record the current time using time.monotonic() as the last time the LED state was changed.
lastChangeTimeLED = time.monotonic()

# Start an infinite loop to repeatedly execute the code within.
while True:
    # Get the current time using time.monotonic().
    timeNow = time.monotonic()

    # Check if the time elapsed since the last LED state change is greater than the blink rate.
    if timeNow - lastChangeTimeLED > blinkRateLED:
        # Invert the LED state using the 'not' keyword.
        led.value = not led.value

        # Update the last LED state change time to the current time.
        lastChangeTimeLED = timeNow
```

Example 2: Detecting “double click” of a button

Background information

- As an illustrative example that might also be useful at some point, here we build up to a program that can tell the difference between a “single click” and a “double click”, just like with a computer mouse.
- I prototyped this using the “Touch Sensor” module from the Connected Interaction Kit. The code could also be applied to a conventional mechanical button, but some modification might be required to address the issue of “bouncing”.

Switch bouncing

Switch bouncing, also known as contact bouncing, is a common issue in electronics where a mechanical switch's contacts do not instantly make or break a connection when the switch is actuated. Instead, the contacts rapidly open and close several times before settling, causing multiple unintended transitions in the signal. This can lead to false readings or undesired behavior in digital circuits or microcontrollers interpreting the switch's state.

- To address this issue, switch debouncing techniques, such as software-based delays or hardware-based filters, are used to ensure stable and accurate signal transitions.
- The Touch Sensor module includes hardware debouncing so it gives a very clean signal.
- We won’t go further into the issue of debouncing here, so just use the Touch Sensor for now.

Program 1: most basic way

The first program (“Button basic.py”) is just included to show the most basic way to control an LED from a button. The LED mirrors the state of the button, so it’s on while you hold the button. See comments in the program for more detailed explanation.

```python
# Import the required libraries:
#   - board: Provides pin definitions specific to the board being used.
#   - digitalio: Provides digital input/output functionality.
#   - time: Provides time-related functions, such as sleep().
import board
import digitalio
import time

# Create a DigitalInOut object for the onboard LED, which is connected to pin D13.
led = digitalio.DigitalInOut(board.D13)

# Set the direction of the 'led' object as OUTPUT, allowing us to control the LED state.
led.direction = digitalio.Direction.OUTPUT

# Create a DigitalInOut object for the button, connected to pin D0.
button = digitalio.DigitalInOut(board.D0)

# Set the direction of the 'button' object as INPUT, allowing us to read its state.
button.direction = digitalio.Direction.INPUT

# Start an infinite loop to repeatedly execute the code within.
while True:
    # Read the current button state and set the LED state to match the button state.
    # If the button is pressed (True), the LED will turn ON.
    # If the button is not pressed (False), the LED will turn OFF.
    led.value = button.value
```

Program 2: edge detection

The second program (“Button toggle single click.py) introduces the concept of **edge detection**. It specifically monitors to changes from **low** to **high** in the state of the button. Each time this occurs, it **toggles** the state of the LED (i.e. turns it on if it was off and vice versa). Again, this is explained in more detail in the comments in the code.

```python
# Import the required libraries:
#   - board: Provides pin definitions specific to the board being used.
#   - digitalio: Provides digital input/output functionality.
#   - time: Provides time-related functions, such as sleep().
import board
import digitalio
import time

# Create a DigitalInOut object for the onboard LED, which is connected to pin D13.
led = digitalio.DigitalInOut(board.D13)

# Set the direction of the 'led' object as OUTPUT, allowing us to control the LED state.
led.direction = digitalio.Direction.OUTPUT

# Create a DigitalInOut object for the button, connected to pin D0.
button = digitalio.DigitalInOut(board.D0)

# Set the direction of the 'button' object as INPUT, allowing us to read its state.
button.direction = digitalio.Direction.INPUT

# Initialize variables to store the last button state and the current LED state.
lastButton = False
LEDstate = False

# Start an infinite loop to repeatedly execute the code within.
while True:
    # Read the current button state and store it in the newButton variable.
    newButton = button.value

    # Check for a rising edge (change from low to high) on the button input.
    if newButton and not lastButton:
        # If a rising edge is detected, toggle the LED state using the 'not' keyword.
        LEDstate = not LEDstate

    # Update the last button state to the current button state.
    lastButton = newButton

    # Set the LED state according to the value of LEDstate.
    led.value = LEDstate
```

Program 3: button toggle using **********************time module**********************

Finally, the third program (“Button toggle only on double click.py”) uses the **time** module (specifically the **time.monotonic()** function) to differentiate between a “double click” (two clicks in sufficiently quick succession – 250ms in the provided code) and one or more “single clicks”. It only toggles the LED state on a double click, but it prints “Single Click” or “Double Click” to the serial monitor. If you were using this as part of a larger program, you could do different actions on the single and double clicks. This one is fairly complicated, but the comments in the code explain in detail.

```python
# Import the required libraries:
import board
import digitalio
import time

# Create a DigitalInOut object for the onboard LED, connected to pin D13.
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT  # Set LED as output

# Create a DigitalInOut object for the button, connected to pin D0.
button = digitalio.DigitalInOut(board.D0)
button.direction = digitalio.Direction.INPUT  # Set button as input

# Initialize variables to track button and LED state, as well as click detection
lastButton = False
LEDstate = False
oneClick = False
clickTime = 0
doubleClickWindow = 0.25  # Time window for double-click detection (in seconds)

# Start an infinite loop to repeatedly execute the code within.
while True:
    newButton = button.value  # Read the current button state

    # Check for a rising edge (change from low to high) on the button input.
    if newButton and not lastButton:
        # If this is the first click, set oneClick to True and save the current time.
        if not oneClick:
            oneClick = True
            clickTime = time.monotonic()
        # If oneClick is already True, a second click has been detected within the time window.
        else:
            print("Double Click")  # Detected a double-click
            oneClick = False  # Reset oneClick for future click detection
            LEDstate = not LEDstate  # Toggle the LED state (if ON, turn OFF; if OFF, turn ON)

    # Update the last button state to the current button state.
    lastButton = newButton

    # Check if the time since the first click has exceeded the double-click window
    # and oneClick is still True (meaning a second click has not been detected).
    if time.monotonic() - clickTime > doubleClickWindow and oneClick:
        print("Single Click")  # Detected a single-click
        oneClick = False  # Reset oneClick for future click detection

    # Set the LED state according to the value of LEDstate.
    led.value = LEDstate
```

[FAQ](https://www.notion.so/FAQ-4d1e68a1814b4fd890f08981efcf8a1b)