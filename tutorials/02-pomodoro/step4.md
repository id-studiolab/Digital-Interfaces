---
layout: default
title: "Step 4: Creating a timer"
parent: "02 Pomodoro"
grand_parent: "Tutorials"

---

# Step 4: Creating a timer
Now we're ready to add in the timer! Import the time library:

```python
##--- Imports
import time

```

We can replace the transition from *state_work* to *state_idle* with a timer. Add the following variables to the program. *work_duration* stores how long we would like *state_work* to last. This is set to 5 seconds. *timer_duration* and *timer_mark* will be used when setting the timer. *timer_mark* will store the starting point of the timer.

```python
##--- Variables
# Timer variables
work_duration = 5
timer_duration = 0
timer_mark = 0

```

With these new variables, we can create a function that starts a new timer. We also create a new function that checks when the timer expires.

```python
##--- Functions
##--- Acting machine effect functions
def set_timer(duration):
    global timer_duration, timer_mark
    timer_duration = duration
    timer_mark = time.monotonic()

##--- Acting machine cause functions
def timer_expired():
    global timer_mark, timer_duration
    if time.monotonic() - timer_mark > timer_duration:
        return True
    else:
        return False

```

After altering the main loop to incoorporate the aforementioned functions, we obtain this:

```python
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

Now, we can switch from *state_idle* to state_work with a button press. Once the button is pressed, a timer starts with the duration of *work_duration*. Once this timer expires, we transition back to *state_idle*.

It's time to upload your code to the ItsyBitsy and see if it works! Your code should now:

 - Output a print statement once the state changes
 - Switch from state_work to state_idle when the timer expires
 - Switch from state_idle to state_work when the button is pressed
 - Turn the LED green when the state changes from idle to work
 - Turn the LED off when the state changes from work to idle
 
[Click here to see the code you should have until now.](step4-code)

[Next Step](step5){: .btn .btn-blue }