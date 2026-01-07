---
layout: default
title: "1: Reaction Game - Hardware and Code"
parent: Assignments
has_children: true
---

# Reaction Game - Hardware and Code
In this weeks assignment we are going to build a simple reaction game. The game consists of two players that wait for a trigger signal after which the first one to push the button is the winner of the game.

Your kit contains a touch sensor that can act as a button but there is only one. So in order to test your game you'll have to borrow a touch sensor or a button from one of your fellow students or the staff. During the next week there will be time for you to go to the PMB and [assemble and solder](https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/assembling-custom-components/tactile-switch) one or two tactile switches from parts available in your Connected Interaction Kit.

## Coding Instructions
In this tutorial, you’ll learn how to set up a CircuitPython program to bring your microcontroller, buttons, and LED to life. We’ll guide you through an example designed to match the behavior outlined in the Acting Machine Diagram (shown below). Take your time to study the code and understand how everything fits together.

As you work through the tutorial, you’ll explore key Python concepts such as declaring variables, using loops (`while`), making decisions with `if` and `elif` statements, and defining and using functions. Additionally, you’ll learn to work with the `neopixel` library to control LED colors, giving your prototype a vibrant and interactive feel.

By the end, you’ll have an understanding of how to run code on your board, how to connect components and a rough idea of how the code is structured.

## Game hardware and control flow
The basic game makes use of two input components (either **Touch Sensor** or **Tactile Switch**), and a **Chainable RGB LED** as an output. 

|   Chainable RGB/W (ChaiNEO)   |          Touch Sensor          |        Tactile Switch         |
| :---------------------------: | :----------------------------: |  :--------------------------: |
| <img src="https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/assets/ChaiNEO-RGBW.png" alt="Chainable RGBW LED" width="200"/> |
<img src="https://id-studiolab.github.io/Connected-Interaction-Kit/components/tactile-switch/assets/custom-tactile-switch-centered.png" alt="Tactile Switch" width="200"/>|
 | <img src="https://id-studiolab.github.io/Connected-Interaction-Kit/components/touch-sensor/assets/Grove-Touch-Sensor.png" alt="Touch Sensor" width="200"/> |
|                               |                  |                    |

Once the LED turns white, both players have to try and touch their sensor as quick as possible. Whoever is faster wins the round, and the LED will light up in the color of the winner.

https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/assets/ChaiNEO-RGBW.png

![](reaction_game.jpg)

The image above shows the minimal components you need to make the technology work. The diagram shows the control flow of the game. We will go into more detail of explaining about <i>Acting Machine Diagrams</i> later. For now you can already interpret how the control might flow if you start in the <i>state</i> (circle) labeled "wait" and then traverse the <i>transitions</i> (arrows) from state to state.

## Game code
There is a simple way to derive a program that implement the control flow from the Acting 
Machine Diagram, we have already done that for you!

In order to navigate to the right code you first have to identify the LED form factor of the LEDs in your Connected Interaction Kit. Match the LED in your kit with one of the images below, then access the game code by pressing the  button under the matching image.

---

|                Chainable RGB/W LED (ChaiNEO)                 |                  Chainable RGB LED (Grove)                   |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| <img src="https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/assets/ChaiNEO-RGBW.png" alt="Chainable RGB LED" width="250"/> | <img src="https://id-studiolab.github.io/Connected-Interaction-Kit/components/chainable-led/assets/Grove-Chainable-LED-2.0.png" alt="Chainable RGB LED" width="250"/> |
|    [Code for the game](game_code_neopixel){: .btn .btn-blue }    |     [Code for the game](game_code_p9813){: .btn .btn-blue }     |

## Extra Challenge: Make It Better!

Congratulations on getting the basic version of the game running! Now it's time to put on your problem-solving hats and improve the game! 
The code you've been working with has a few intentional bugs. One key challenge involves the way button presses are handled:

Hint: If you keep a button pressed before the LED turns white, you’ll always win. That doesn't sound very fair, does it?

Your task is to identify and fix this bug so the game works as intended.
Look through the code and think of how you could achieve this, maybe also penalizing a player if they press the button before the led turns white!
