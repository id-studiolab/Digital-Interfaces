---
layout: default
title: "Step 5: Adding an alarm"
parent: "02 Pomodoro"
grand_parent: "Tutorials"

---

# Step 5: Adding an alarm
Switching between states works now, as does the LED. But when the user's worktime is over, they aren't alerted in any way before the LED turns off and the state switches. To make the user aware of their worktime being over, we should add an alarm. First, we add a new state, *state_break_alarm*. When we are in *state_work* and the timer expires, we go to *state_break_alarm*. We also color the LED red.

```python
##--- Imports
from analogio import AnalogOut

##--- Variables
# State variables
state_break_alarm = 2

##--- Main loop
while True:
    # State Idle
    if current_state == state_idle:
        if check_button_press():
            current_state = state_work
            set_led_color(led_green)
            set_timer(work_duration)

    # State Work
    elif current_state == state_work:
        if timer_expired():
            current_state = state_break_alarm
            set_led_color(led_red)
    
    # State Break Alarm
    elif current_state == state_break_alarm:
        if check_button_press():
            current_state = state_idle
            set_led_color(led_off)

```

Now that we've set up the break state, we are ready to implement the actual alarm. We'll use a buzzer for this. Attach the buzzer to A0. We'll need to import the AnalogOut function to send information to the buzzer.

Then, we also need to write a function that can turn the buzzer on and off. We will be able to pass a value on to this *set_buzzer()* function. If this value is True, we write 65535 to the buzzer. 65535 is the largest number (and thus, voltage) we can read or output to an Analog port. If we pass False to this function, we write 0 to the buzzer instead.

```python
##--- Variables
# Buzzer variables
buzzerpin = board.A0
buzzer = AnalogOut(buzzerpin)

##--- Functions
##--- Acting machine effect functions
def set_buzzer(value):
    if value == True:
        buzzer.value = 65535
    else:
        buzzer.value = 0

```

Let's alter the main loop to incorporate the buzzer, passing True and False to the function wherever the buzzer needs to turn on and off:

```python
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
            current_state = state_idle
            set_led_color(led_off)
            set_buzzer(False)

```

It's time to upload your code to the ItsyBitsy and see if it works! Your code should now:

 - Turn the LED green when switching to state_work
 - Turn the LED red and turn on the buzzer when switching to state_break_alarm
 - Return to state_idle when pressing the button while in state_break_alarm
 
[Click here to see the code you should have until now.](step5-code)

[Next Step](step6){: .btn .btn-blue }