---
layout: default
title: "4: Walkie-Talkie"
parent: Assignments
has_children: false
---

# Walkie-Talkie
In this week's assignment we are going to build-up from the knowledge learned last week from using MQTT, and we will expand it by also publishing on the server!
The goal is to build a walkie-talkie that can both send and receive messages from other boards.

---

## Coding Instructions
In this assignment you will learn how to publish data to an MQTT topic and revise last week's assignment on how to process received data.

When connected to an MQTT server, we can not only listen to a topic (e.g. "perlin" and "iss/distance" from last week), but also send data to it!
The act of sending data is called "publishing" and when doing so, all devices which are connected to the topic you're sending information to will receive the data you send.

---

## Coding Assignment
Your goal is to implement 2 buttons and an actuator of your choice (we recommend either a piezo buzzer or a vibration motor), in the following way:
- 1 button dedicated to opening the walkie-talkie channel
- 1 button to send messages on the channel
- 1 actuator that is triggered when a message is received

Remember that walkie-talkies cannot receive messages while their channel is open.

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
state_listening = 1
state_speaking = 2

current_state = 0

# Define variable to save data received from the MQTT broker
last_received_value = 0

##--- Button variables

# Define the open channel button variable and assign it to port D13 of our board
open_channel_button = digitalio.DigitalInOut(board.D13)

# Define the speak button variable and assign it to port D7 of our board
speak_button digitalio.DigitalInOut(board.D7)

## Define the buttons as an input component
open_channel_button.direction = digitalio.Direction.INPUT
speak_button.direction = digitalio.Direction.INPUT

##--- Actuator variables
actuator = digitalio.DigitalInOut(board.D4)
actuator.direction = digitalio.Direction.OUTPUT

#actuator = pwmio.PWMOut(board.D4, variable_frequency=True)

##--- MQTT configuration

# Define variable to save data received from the MQTT broker
last_received_value = 0
   
# Method used when the board receives 
# a message from the MQTT server.
def handle_message(client, topic, msg):
   global last_received_value

   # Assign message received to last_received variable
   last_received_value = msg

   # See what was printed and on what topic
   print("New message on topic {0}: {1}".format(topic, msg))

# You can find the client Id in the settings.py this is used to identify the board
client_id = settings["mqtt_clientid"]

# Here you should select the topic of the person you want to talk to.
# They should set as listen_topic the topic to which you're sending messages to.
mqtt_listen_topic = "ItsyBitsy Studiolab"
mqtt_speak_topic = "TOPIC YOU WANT TO PUBLISH TO HERE"

# Create a mqtt connection based on the settings file.
mqtt_client = Create_MQTT(client_id, handle_message)

# Listen for messages on the topic specified above
mqtt_client.subscribe(mqtt_listen_topic)

##--- Main loop

while True: 

   # -------------------------------------------------------------| 
   #                                                              | 
   # Use the Acting Machine Diagram to program your solution here | 
   #                                                              | 
   # -------------------------------------------------------------|

   message = "ping"

   # mqtt_client.publish(message, mqtt_speak_topic)

   print(last_received_value)
   
   # Sleep for a bit to make the keypress events occur at a human timescale 
   # Skilled gamers can do ~7 button presses per second (says ChatGPT) 
   time.sleep(0.143)

```


--- 

## Extra Challenge: Interpret received messages 
TBI