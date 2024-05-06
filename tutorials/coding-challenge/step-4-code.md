---
layout: default
title: "Step 4: Code until now"
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
import random

# Register sensors
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT

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

triggerd = False

color_list = []

while True:
    # Replay
    if button.value is True:
        for color in color_list:
            leds.fill(color)
            leds.show()
            time.sleep(1)
        leds.fill(color_off)
        leds.show()
        color_list = []
    
    # Turn on LED
    if sound_sensor.value > 30000 and not triggerd:
        triggerd = True
        color = (random.randint(0,70),random.randint(0,70),random.randint(0,70),0)
        print(f"{color}")
        color_list.append(color)
        leds.fill(color)
        leds.show()
        timer_mark = time.monotonic()
        # Don't over trigger
        time.sleep(0.2)
        
    if sound_sensor.value < 30000 and triggerd:
        triggerd = False

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
import random

# States
state_on_loud = 0
state_on_quiete = 1
state_off = 2
state_memory = 3
current_state = state_off


# Register sensors
button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT

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

color = None
triggered = False

color_memory = []

while True:
    
    if current_state == state_off:
        # make sure the LED is off
        leds.fill(color_off)
        leds.show()
        # check if we should turn on
        if sound_sensor.value > 30000:
            # Start the timer!
            color = (random.randint(0,70),random.randint(0,70),random.randint(0,70),0)
            color_memory.append(color)
            timer_mark = time.monotonic()
            current_state = state_on_loud
        elif button.value is True:
            current_state = state_memory
    
    elif current_state == state_on_loud:
        leds.fill(color)
        leds.show()
        if time.monotonic() - timer_mark >= timer_duration:
            current_state = state_off
        elif button.value is True:
            current_state = state_memory
        elif sound_sensor.value < 25000:
            current_state = state_on_quiete
        
            
    elif current_state == state_on_quiete:
        leds.fill(color)
        leds.show()
        if time.monotonic() - timer_mark >= timer_duration:
            current_state = state_off
        elif button.value is True:
            current_state = state_memory
        elif sound_sensor.value > 30000:
            # Her start the timer!
            color = (random.randint(0,70),random.randint(0,70),random.randint(0,70),0)
            color_memory.append(color)
            timer_mark = time.monotonic()
            current_state = state_on_loud
    elif current_state == state_memory:
        for color in color_memory:
            leds.fill(color)
            leds.show()
            time.sleep(1)
        leds.fill(color_off)
        leds.show()
        color_memory = []
        current_state = state_off
````