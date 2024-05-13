---
layout: default
title: "Step 6: Adding the breaks"
parent: "02 Pomodoro"
grand_parent: "Tutorials"

---

# Step 6: Adding the breaks
## Step 6.1 Short break
Instead of returning to state_idle, we want to give the user a timed break, which can be either a short break or a long break. We start with the short break. Add *state_short_break* to your variables. When the break is over, we also want to alert the user that their break is over. This state, *state_work_alarm*, should also be in your list of variables. We also store its duration in a variable called *short_break_duration*. It is set to three seconds now:

```python
##--- Variables
# State variables
state_short_break = 3
state_work_alarm = 4

# Timer variables
short_break_duration = 3

```

The functions that we made in the last steps should be enough to implement the behavior we want. We need to add two more elif statements to take the two new states into account. The program should enter *state_short_break* when *state_break_alarm* is over, and go into *state_work_alarm* when the break is over. From *state_work_alarm*, it should return to *state_work*. We can make use of the different LED colors to differentiate between all these states. 

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
            current_state = state_short_break
            set_led_color(led_blue)
            set_timer(short_break_duration)
            set_buzzer(False)

    # State Short Break
    elif current_state == state_short_break:
        if timer_expired():
            current_state = state_work_alarm
            set_led_color(led_yellow)
            set_buzzer(True)

    # State Work Alarm
    elif current_state == state_work_alarm:
        if check_button_press():
            current_state = state_work
            set_led_color(led_green)
            set_timer(work_duration)
            set_buzzer(False)

```

It's time to upload your code to the ItsyBitsy and see if it works! Your code should now:

 - Have the LED turn a different color upon entering a new state
 - Sound the alarm in states state_break_alarm and state_work_alarm
 - Give the user a timed break 
 
 Here you can find the code we have until now: ** add link ** 

## Step 6.2 Long break
After three short breaks, we want to give the user a long break before they have to go back to work. We need to take into account how many breaks the user has had. Create a new variable called *break_counter*, a new state called *state_long_break*, and a variable for the duration:

```python
##--- Variables
break_counter = 0

# State variables 
state_long_break = 5

# Timer variables
long_break_duration = 8

```

Now we need to go into *state_break_alarm* and count the amount of times that the alarm has gone off. If this number is less than 3, we enter *state_short_break*. If it's 3 or more, we reset the *break_counter* back to 0 and enter *state_long_break*.

```python
# State Break Alarm
    elif current_state == state_break_alarm:
        if check_button_press():
            set_buzzer(False)
            if break_counter < 3:
                current_state = state_short_break
                set_led_color(led_blue)
                set_timer(short_break_duration)
                break_counter = break_counter + 1
            else:
                current_state = state_long_break
                set_led_color(led_white)
                set_timer(long_break_duration)
                break_counter = 0

```

Now we can add in the behavior for the long break. When the timer runs out, we want to turn off the Pomodoro timer and return to *state_idle*:

```python
# State Long Break
    elif current_state == state_long_break:
        if timer_expired():
            current_state = state_idle
            set_led_color(led_off)
            set_buzzer(False)

```

And here we have a functional Pomodoro timer! Upload your code to the ItsyBitsy and see if it works. 

[Click here to see the code you should have until now.](step6-code)

[Next Step](step7){: .btn .btn-blue }