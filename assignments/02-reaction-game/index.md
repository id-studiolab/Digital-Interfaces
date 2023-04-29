---
layout: default
title: "2: Reaction Game"
parent: Assignments
has_children: true
---

# Reaction Game
In this weeks assignment we are going to build a simple reaction game and embody it in different shapes and forms.


## Game hardware and control flow
The basic game makes use of two input components (either Touch Sensor or Tactile Switch), and a Chainable RGB LED as an output. 

Once the LED turns white, both players have to try and touch their sensor as quick as possible. Whoever is faster wins the round, and the LED will light up in the color of the winner.

![](reaction_game.jpg)

The image above shows the minimal components you need to make the technology work. The diagram shows the control flow of the game. We will go into more detail of explaining about <i>Acting Machine Diagrams</i> later. For now you can already interprete how the control might flow if you start in the <i>state</i> (circle) labeled "wait" and then traverse the <i>transitions</i> (arrows) from state to state.

## Game code
There is a simple way to derive a program that implement the control flow from the Acting 
Machine Diagram, we have already done that for you!

In order to navigate to the right code you first have to identify the LED form factor of the LEDs in your Connected Interaction Kit. Match the LED in your kit with one of the images below, then access the game code by pressing the  button under the matching image.

---

|                Chainable RGB/W LED (ChaiNEO)                 |                  Chainable RGB LED (Grove)                   |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/assets/ChaiNEO-RGBW.png" alt="Chainable RGB LED" width="250"/> | <img src="https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/assets/Grove-Chainable-LED-2.0.png" alt="Chainable RGB LED" width="250"/> |
|    [Code for the game](game_code_neopixel){: .btn .btn-blue }    |     [Code for the game](game_code_p9813){: .btn .btn-blue }     |
