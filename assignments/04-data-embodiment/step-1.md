---
layout: default
title: "Step 1: Setting up MQTT on your ItsyBitsy"
parent: "Week 4: Data Embodiment"
grand_parent: Assignments
has_children: false
---

# Step 1: Setting up MQTT on your ItsyBitsy

After successfully completing [Tutorial 4](https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/03-connect-to-the-internet/) and connected your ItsyBitsy to the Internet, follow the steps below to establish a basic MQTT connection with our MQTT server.

1. Download the [Circuit Python library bundle for Version 9.x](https://circuitpython.org/libraries) if you haven’t already. Do not copy the entire .zip bundle to your CIRCUITPY device! Instead copy over only the specific library folders that you need for this assignment. They are referenced in this tutorial. 
2. Search for `adafruit_minimqtt` and copy the whole `adafruit_minimqtt` library folder into the `lib` folder of your `CIRCUITPY` device
3. Extend your `secrets.py` file and add the entries for the MQTT broker (the server we connect to), your username (please construct it as **Studio[your studio]_YourName**), and add the access token below. Save the file afterwards.
   ```python
   secrets = {
      'ssid' : 'TUD-facility', # The wifi we connect to 
      'password' : 'replace-with-your-iPSK-String', # Our personal password to connect to Wifi
      'mqtt_broker' : 'ide-education.cloud.shiftr.io', # The MQTT server we connect to
      'mqtt_broker_user' : 'ide-education', # The username for connecting to the server
      'mqtt_broker_password' : '9RI9jcOCtnoIAESq', # The password for connecting to the server
      'mqtt_clientid': 'Studio5_Caspar', # The device name we present to the server when connecting
   }
   ```
4. Download the MQTT wrapper from this link: [#TODO: add link]() and add it to your `lib` folder.

   Open a new `code.py` file and copy the following code. 

   ```python
   # Connect the client to the MQTT broker.
   import MQTT_wrapper
   import connect_to_wifi

   # Connect to wifi

   # Subscribe to topic

   # listen for messages
      
   # --- Main loop
   while True:
      # This try / except loop is used to continuously get new data from MQTT, and reset if anything goes wrong
      try:
         mqtt_client.loop(0.1)
      except (ValueError, RuntimeError) as e:
         print("Failed to get data, retrying\n", e)
         wifi.reset()
         mqtt_client.reconnect()
         continue
         
         
      # Add your own looping functions to do something with the data below this line
         
      # Let's print the incoming data in our Serial Monitor
      print(last_incoming_value)
      
      time.sleep(0.01)

   ```

5. How to get messages...

[Previous Step](index){: .btn .btn-gray }  [Next Step](step-2){: .btn .btn-blue }
