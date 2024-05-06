---
layout: default
title: "Step 1: Code until now"
parent: "Coding Challenge"
nav_exclude: true
---

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

while True:
    if sound_sensor.value > 30000:
        leds.fill(color_on)
        leds.show()
        time.sleep(1)
        leds.fill(color_off)
        leds.show()
````