---
layout: default
title: "Coding Challenge"
has_children: false
parent: "Tutorials"
---

# Coding Challenge - Sound sensitive light

This section is not a full tutorial but more a challenge of you coding skills. You will be building an increasingly more complicated sound activated LED. Every step consists of the following:

- A detailed explanation of what the end result of this step should be.
- A button that leads to a page with the solution.

We really encourage you to try before taking a peak at the hints and solution.
If you get stuck on a step then don't forget to check the solutions to a previous step before checking the solution of the current step, as it might help you solve it on your own.



## Step 1 - Sound activated LED

For the first step you are going to create a sound activated LED. For this LED we will be using the [Neopixel Chainable LED](https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/chainable-led-chaineo) and the [Sound Sensor](https://id-studiolab.github.io/Connected-Interaction-Kit/components/sound-sensor/sound-sensor).
We want the sound sensor to trigger when it's value exceeds `30000` and the led should stay on for `1` second. The color of the LED should be a dim white with the value of `(0,0,0,50)`.

Do not forget to turn of the LED at the start of you code.

[Show Solution](step-1-code){: .btn .btn-blue }

## Step 2 - No sleep for the wicked

There is a good change that in Step 1 you used `time.sleep()` in order to make the LED stay on for one second.
For this next step we challenge you to improve your code to no longer use any `time.sleep()`.
Removing the `time.sleep()` will allow us to preform more multitasking in the next steps.

[Show Solution](step-2-code){: .btn .btn-blue }

## Step 3 - Taste the rainbow
For this step we want to change the behaviour of the LED. Every time the sound sensor triggers, the LED should light up with a random color.

An important part of this is that for every trigger it should only pick one color. Meaning that if I were to snap my fingers and it picks a color it should only pick a new color after it has become quite again (a sensor value of less than `30000`).

A good way to test this is by printing every color picked to the serial monitor!

[Show Solution](step-3-code){: .btn .btn-blue }

## Step 4 - Perfect Memory
For our final step, we are going to add a button. When the user presses the button, the following should happen:
It should show every color chosen since the board started for 1 second each. After having shown all the colors, it should forget them.
So, suppose the sensor has been triggered three times since the restart and shows red, purple, and orange. In that case, if the user presses the button, it should show red for one second, purple for one second, and orange for one second.

You are allowed to use `time.sleep()` here again.

[Show Solution](step-4-code){: .btn .btn-blue }