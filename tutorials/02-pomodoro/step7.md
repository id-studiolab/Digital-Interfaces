---
layout: default
title: "Step 7: Additional visualization using the servo"
parent: "02 Pomodoro"
grand_parent: "Tutorials"

---

# Step 7: Additional visualization using the servo
The Pomodoro timer is functional, but we can still improve on the user experience. It would be a good idea to visualize to the user how much time there is left before the next alarm goes off. We can use a servo for this, with its angle being 0 when the timer just starts, going up to 180 when the timer expires.

Import the following libaries:

```python
import pwmio
from adafruit_motor import servo

```

Then, add the following variables to the program:

```python
# Servo variables
pwm = pwmio.PWMOut(board.D13, frequency = 50)
my_servo = servo.Servo(pwm)

```

Attach the servo to pin D13. We can now control the servo through the *my_servo* variable. Let's create a function that updates the servo's angle. This function should look at the timer variables, *timer_mark* and *timer_duration*, as well as the current time, and map these to an angle.

We do this by subtracting the minimum time value (*timer_mark*) from the current time. Then we divide this result by the timer's duration. This will give us a number between 0 and 1.

Multiplying this by our new maximum value, 180, will give us a number between 0 and 180, which we can use as an angle for the servo. Since we only want to use whole numbers, we cast it to an integer before saving it into the angle variable.

```python
##--- Acting machine effect functions
def update_servo_angle():
    current_time = time.monotonic()
    if current_time < timer_mark + timer_duration:
        angle = int((current_time - timer_mark) / timer_duration * 180)
        my_servo.angle = angle 

```

We can call this function in every state we have a timer in: *state_work*, *state_short_break*, and *state_long_break*.

Upload your code to the ItsyBitsy and see if it works. This concludes the programming part of the assignment! 

[Click here to see the code you should have until now.](step7-code)

[Last Step](step8){: .btn .btn-blue }