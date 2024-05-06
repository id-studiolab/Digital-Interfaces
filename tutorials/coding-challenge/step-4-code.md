---
layout: default
title: "Step 4: Code until now"
parent: "Coding Challenge"
nav_exclude: true
---

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