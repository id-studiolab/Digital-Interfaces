---
layout: default
title: "Step 1: Setting up MQTT on your ItsyBitsy"
parent: "Week 4: Data Embodiment"
grand_parent: Assignments
has_children: false
---

# Step 1: Setting up MQTT on your ItsyBitsy

After successfully completing [Tutorial 4](https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/03-connect-to-the-internet/) and connected your ItsyBitsy to the Internet, follow the steps below to establish a basic MQTT connection with our MQTT server.

{: .note }
If you followed the tutorial for connecting your board to the WiFi you should already have a folder called `adafruit_esp32spi`, double check and if you don't have it be sure to get it from the bundle listed below in point 1.

{: .warning } 
Do not copy the entire .zip bundle to your CIRCUITPY device! Instead copy only the specific libraries and folders that you need for this assignment. They are referenced in the steps below. 

1. Download the [Circuit Python library bundle for Version 9.x](https://circuitpython.org/libraries) if you haven’t already. 

2. Search for `adafruit_minimqtt` and copy the whole `adafruit_minimqtt` folder into the `lib` folder of your `CIRCUITPY` device.

3. Extend your `secrets.py` file and add the entries for the MQTT broker (the server we connect to), your username (please construct it as **Studio[your studio]_YourName**), and add the access token below. Save the file afterwards.
   ```python
   secrets = {
      'ssid' : 'TUD-facility', # The wifi we connect to 
      'password' : 'replace-with-your-iPSK-String', # Our personal password to connect to Wifi
      'mqtt_broker' : 'ide-education.cloud.shiftr.io', # The MQTT server we connect to
      'mqtt_user' : 'ide-education', # The username for connecting to the server
      'mqtt_password' : '9RI9jcOCtnoIAESq', # The password for connecting to the server
      'mqtt_clientid': 'Studio5_Caspar', # The device name we present to the server when connecting
   }
   ```
4. Download the MQTT wrapper using the button below and add it to your `lib` folder.
[Download MQTT wrapper](MQTT.zip){: .btn .btn-blue }

   Open a new `code.py` file and copy the following code. 

   ```python
   ##--- Library Imports
   import time
   import digitalio
   import board

   from MQTT import Create_MQTT
   from settings import settings

   ##--- Defining states
   state_wait = 0
   current_state = 0

   # Define variable to save data received from the MQTT broker
   last_received_value = 0
      
   ##--- MQTT Setup

   # Method used when the board receives 
   # a message from the MQTT server.
   def handle_message(client, topic, msg):
      global last_received_value

      # Assign message received to last_received variable
      last_received_value = msg

      # See what was printed and on what channel
      print("New message on topic {0}: {1}".format(topic, msg))

   # You can find the client Id in the settings.py this is used to identify the board
   client_id = settings["mqtt_clientid"]

   # Here you can choose what topic you want to subscribe to. The default is Perlin Noise.
   # Make sure there is only one topic active at any given time (and otherwise add a # before the one you do not want to use anymore)
   MQTT_topic = "perlin"
   #MQTT_topic = "iss/distance"
   #MQTT_topic = "iss/location

   # Create a mqtt connection based on the settings file.
   mqtt_client = Create_MQTT(client_id, handle_message)

   # Listen for messages on the topic specified above
   mqtt_client.subscribe(MQTT_topic)


   # --- Main loop
   while True:
      # This try / except loop is used to continuously get new data from MQTT, and reset if anything goes wrong
      try:
         mqtt_client.loop(0.1)

      except (ValueError, RuntimeError) as e:
         print("Failed to get data, retrying\n", e)
         mqtt_client.reconnect()
         continue
         
      if current_state is state_wait:
         # Let's print the received data in our Serial Monitor
         print(last_received_value)

         # ---------------------------------------------------| 
         #                                                    | 
         # Use last_received_variable in your code to use     | 
         # the data received from the MQTT broker.            | 
         #                                                    | 
         # ---------------------------------------------------|
      
      time.sleep(0.01)

   ```

5. With the code above we connect to an MQTT client, specify the **topic** and listen to the data being sent to it.
If you want to process the data received you can use the `last_received_value` variable in the `while True` loop.

| Acting Machine Diagram | 
| -------------------------------------- | 
| ![](data_embodiment_state_diagram.png)                | 

| Acting Machine Diagram | 
| -------------------------------------- | 
| <div style="text-align: center;">
    <img src="data_embodiment_state_diagram.png" alt="Data Embodiment Acting Machine Diagram" style="width:50%;">
  </div>|
| Nog wat Text |

In the next page we show some useful functions on how to process the data received.

[Previous Step](index){: .btn .btn-gray }  [Next Step](step-2){: .btn .btn-blue }
