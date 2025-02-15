---
layout: default
title: "5: Walkie-Talkie"
parent: Assignments
has_children: false
---

# Walkie-Talkie
In this week's assignment we are going to build-up from the knowledge learned last week on MQTT, and we will expand it by also publishing on the server!
The goal is to build a walkie-talkie that can both send and receive messages from other boards.

---

## Coding Instructions
In this assignment you will learn how to publish data to an MQTT topic and revise last week's assignment on how to process received data.

When connected to an MQTT server, we can not only listen to a topic (e.g. "perlin" and "iss/distance" from last week), but also send data to it!
Sending data to the MQTT broker is called "publishing" and when doing so, all devices which are connected to the topic you're sending information to will receive the data you send.

---

## Coding Assignment
Your goal is to implement 2 buttons and an actuator of your choice (we recommend either a piezo buzzer or a vibration motor), in the following way:
- 1 button dedicated to opening the walkie-talkie channel
- 1 button to send messages on the channel
- 1 actuator that is triggered when a message is received

**Remember that walkie-talkies cannot receive messages while their channel is open.**

Just like last week, here below we present a template with **almost** everything you need to make your walkie-talkie work. 
Although, one crucial part is **missing**, the part inside the `while` loop.

Your assignment is to use the template code and one of the acting machine diagrams here below to create a working controller.

| Acting Machine Diagram | 
| -------------------------------------- | 
| TODO: Insert image                | 


### Code template
```python
##--- Library Imports
import time
import digitalio
import board

from MQTT import Create_MQTT
from settings import settings

##--- Defining states
state_idle = 0
state_receiving = 1
state_channel_open = 2
state_transmitting = 3

current_state = 0

# Define variable to save data received from the MQTT broker
last_received_value = 0

##--- Button variables

# Define the open channel button variable and assign it to port D13 of our board
open_channel_button = digitalio.DigitalInOut(board.D13)

# Define the speak button variable and assign it to port D7 of our board
speak_button = digitalio.DigitalInOut(board.D7)

## Define the buttons as an input component
open_channel_button.direction = digitalio.Direction.INPUT
speak_button.direction = digitalio.Direction.INPUT

##--- Actuator variables
actuator = digitalio.DigitalInOut(board.D4)
actuator.direction = digitalio.Direction.OUTPUT

# For more information on how to use PWM check this link: 
# https://id-studiolab.github.io/Connected-Interaction-Kit/components/piezo-buzzer/piezo-buzzer.html#define-a-tone-using-pulse-width-modulation-pwm

#actuator = pwmio.PWMOut(board.D4, variable_frequency=True)

##--- MQTT configuration

# Define variable to save data received from the MQTT broker
last_received_value = 0
device_has_received_new_value = False
   
# Method used when the board receives a message from the MQTT server.
def handle_message(client, topic, msg):
    global last_received_value
    global device_has_received_new_value

    # Assign message received to last_received variable
    last_received_value = msg

    device_has_received_new_value = True


# You can find the client Id in the settings.py this is used to identify the board
client_id = settings["mqtt_clientid"]

# Create a mqtt connection based on the settings file.
mqtt_client = Create_MQTT(client_id, handle_message)

# Here you should select the topic of the person you want to talk to.
# Write the topic you want to send messages to.
mqtt_speak_topic = "MySpeakTopic"

# You should set as "listen_topic" their "speak_topic" and vice-versa
mqtt_listen_topic = "MyListenTopic"


# Listen for messages on the topic specified above
mqtt_client.subscribe(mqtt_listen_topic)

##--- Main loop
while True: 
    try:
        mqtt_client.loop(0.1)

    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        mqtt_client.reconnect()
        continue
    # ---------------------------------------------
    # ^ DO NOT CHANGE ANYTHING ABOVE THIS POINT ^ |
    # ---------------------------------------------

    message = "ping"

    # Use this method to publish messages on a topic:
    # mqtt_client.publish(mqtt_speak_topic, message)

    # ----------------------------------------------------------------| 
    #                                                                 | 
    # Use the Acting Machine Diagram to program your solution here    | 
    #                                                                 |
    # Hint: Make use of the "device_has_received_new_value" variable  |
    #                                                                 | 
    # ----------------------------------------------------------------|

    # ----------------------------------------------
    # v DO NOT CHANGE ANYTHING BELOW THIS POINT v  |
    # ----------------------------------------------
    device_has_received_new_value = False
    time.sleep(0.1)
```

--- 

## Extra Challenge: Interpret received messages 

In the current assignment, your walkie-talkie sends a fixed message ("ping") each time you press the button. But real communication isn't just about sending the same thing over and over; messages can carry different meanings!  

For this challenge, modify your code so that different messages can be sent instead of always sending "ping". 
Think about the different ways in which you could send different messages, for example, assign two buttons or create a switch to select messages before sending. 

When receiving messages, be sure that your board also interprets incoming messages and responds differently based on their content.

Think about how this could enhance the interaction, different messages could trigger different responses from the actuator, maybe also triggering different actuators.

Push yourself to explore how MQTT can be used for more dynamic communication!