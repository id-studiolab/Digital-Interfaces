---
layout: default
title: "Step 1: Setting up MQTT on your ItsyBitsy"
parent: "Week 4: Data Embodiment"
grand_parent: Assignments
has_children: false
---

# Step 1: Setting up MQTT on your ItsyBitsy

After successfully completing [Tutorial 4](https://id-studiolab.github.io/Connected-Interaction-Kit/tutorials/03-connect-to-the-internet/) and connected your ItsyBitsy to the Internet, follow the steps below to establish a basic MQTT connection with our MQTT server.

1. Download the [Circuit Python library bundle for Version 7.x](https://circuitpython.org/libraries) if you haven’t already. Do not copy the entire .zip bundle to your CIRCUITPY device! Instead copy over only the specific library folders that you need for this assignment. They are referenced in this tutorial. 
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
4. This week we are introducing a new way of choosing what code should be executed on your ItsyBitsy. We think that this will help you when juggling or working on multiple prototypes or code tryouts at the same time.

   Create a new file called `mqtt_client.py` and paste the following code into it. It looks like a bunch, but you don’t have to worry about most of it. Save the file on your `CIRCUITPY` device.

   ```python
   # --- Imports
   import time
   import board
   import busio
   from digitalio import DigitalInOut
   from adafruit_esp32spi import adafruit_esp32spi
   from adafruit_esp32spi import adafruit_esp32spi_wifimanager
   import adafruit_esp32spi.adafruit_esp32spi_socket as socket
   import adafruit_minimqtt.adafruit_minimqtt as MQTT
   
   #################################################################
   ################# SETTING UP WIFI AND MQTT ######################
   #################################################################
   
   # --- WIFI Setup
   
   # Get wifi details and more from a secrets.py file
   try:
      from secrets import secrets
   except ImportError:
      print("WiFi secrets are kept in secrets.py, please add them there!")
      raise
   
   # If you have an externally connected ESP32:
   esp32_cs = DigitalInOut(board.D9)               # Chip select pin
   esp32_ready = DigitalInOut(board.D11)           # BUSY or READY pin
   esp32_reset = DigitalInOut(board.D12)           # Reset pin
   
   spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
   esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
   
   wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets)
   
   # --- MQTT Functions
   
   # Define callback methods which are called when events occur
   # pylint: disable=unused-argument, redefined-outer-name
   def connected(client, userdata, flags, rc):
      # This function will be called when the client is connected
      # successfully to the broker.
      print("Connected to MQTT broker! Listening for topic changes on %s" % MQTT_topic)
      # Subscribe to all changes on the default MQTT topic feed.
      client.subscribe(MQTT_topic)
   
   def disconnected(client, userdata, rc):
      # This method is called when the client is disconnected
      print("Disconnected from MQTT Broker!")
   
   def message(client, topic, message):
      global last_incoming_value
      """Method callled when a client's subscribed feed has a new
      value.
      :param str topic: The topic of the feed with a new value.
      :param str message: The new value
      """
      print("New message on topic {0}: {1}".format(topic, message))
      
      # Check if we are recieving messages from ISS -> Location, that message contains two values
      if " " in message:
          last_incoming_value = message.split()
          # make a number out of the message
          last_incoming_value[0] = float(last_incoming_value[0])
          last_incoming_value[1] = float(last_incoming_value[1])
      else:
          # make a number out of the message
          last_incoming_value = float(message)
   
   # Connect to WiFi
   print("Connecting to WiFi...")
   wifi.connect()
   print("Connected!")
   
   # Initialize MQTT interface with the esp interface
   MQTT.set_socket(socket, esp)
   
   # Set up a MiniMQTT Client
   mqtt_client = MQTT.MQTT(
      broker=secrets["mqtt_broker"], username=secrets["mqtt_broker_user"], password=secrets["mqtt_broker_password"], client_id = secrets["mqtt_clientid"]
   )
   
   # Setup the callback methods above
   mqtt_client.on_connect = connected
   mqtt_client.on_disconnect = disconnected
   mqtt_client.on_message = message
   
   #################################################################
   ############## WRITE YOUR OWN CODE BELOW THIS LINE ##############
   #################################################################
   
   # --- Variables
   
   # Here you can choose what datasource you want to subscribe to. The default is Perlin Noise.
   # Make sure there is only one datasource active at any given time (and otherwise add a # before the one you do not want to use anymore)
   
   MQTT_topic = "perlin"
   #MQTT_topic = "iss/distance"
   #MQTT_topic = "iss/location"
   
   # We will use this value to save new incoming data
   last_incoming_value = 0
   
   ## --- Functions
   
   # --- Setup
   
   # Connect the client to the MQTT broker.
   print("Connecting to MQTT broker...")
   mqtt_client.connect()
   mqtt_client._backwards_compatible_sock = True
   
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
   
5. The ItsyBitsy always looks for the file `code.py` to run code. By passing the following one line in our `code.py` file and saving it, we instruct our ItsyBitsy to run all code found in the  `mqtt_client.py` file that we created in the previous step
   
   ```python
   import mqtt_client
   ```
   
   The benefit is that we keep our `code.py` tidy, and can quickly switch between different code iterations like so:
   
   ```python
   # Comment or uncomment the file you want to run
   #import mqtt_client
   import mqtt_led_color
   #import mqtt_servo_motor
   ```

6. Let’s `import mqtt_client` for now and save the file. Open the `Serial Monitor` and you should be receiving data!

[Previous Step](index){: .btn .btn-gray }  [Next Step](step-2){: .btn .btn-blue }
