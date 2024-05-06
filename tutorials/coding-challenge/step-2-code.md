---
layout: default
title: "Step 2: Code until now"
parent: "Coding Challenge"
nav_exclude: true
---

## Without Statemachine
````python
import time
import board
import analogio
import digitalio
import neopixel

# Register sensors
sound_sensor = analogio.AnalogIn(board.A0)

# Register LED
leds = neopixel.NeoPixel(board.D13, 1, auto_write=False, pixel_order=neopixel.GRBW)

# colors
color_off = (0,0,0,0)
color_on = (0,0,0,10)

leds.fill(color_off)
leds.show()

timer_mark = 0
timer_duration = 1

while True:
    # Turn on LED
    if sound_sensor.value > 30000:
        leds.fill(color_on)
        leds.show()
        timer_mark = time.monotonic()

    # Turn LED off
    if time.monotonic() - timer_mark >= timer_duration:
        leds.fill(color_off)
        leds.show()

````

## With statemachine
````python
import time
import board
import analogio
import digitalio
import neopixel

# States
state_on = 0
state_off = 1
current_state = 0


# Register sensors
sound_sensor = analogio.AnalogIn(board.A0)

# Register LED
leds = neopixel.NeoPixel(board.D13, 1, auto_write=False, pixel_order=neopixel.GRBW)

# colors
color_off = (0,0,0,0)
color_on = (0,0,0,10)

leds.fill(color_off)
leds.show()


timer_mark = 0
timer_duration = 1

while True:
    
    if current_state == state_off:
        # make sure the LED is off
        leds.fill(color_off)
        leds.show()
        # check if we should turn on
        if sound_sensor.value > 30000:
            # Start the timer!
            timer_mark = time.monotonic()
            current_state = state_on       
    
    elif current_state == state_on:
        leds.fill(color_on)
        leds.show()
        if time.monotinic() - timer_mark >= timer_duration:
            current_state = state_off
````