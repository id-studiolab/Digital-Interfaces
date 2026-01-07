---
layout: default
title: "Step 4 (Example): Creating a Philips Hue Light"
parent: "Week 4: Data Embodiment"
grand_parent: Assignments
has_children: false
---

# Step 4 (Example): Creating a Philips Hue Light

## Create your own Shiftr.io Environment
1. Go to [Shiftr.io](https://www.shiftr.io) and create a new account
2. Deloy a new instance and open the instance in a new window. You will see a green background with our MQTT broker on top.
3. Create a new access token that you can use to connect new devices by clicking on the Gear Icon in the bottom right corner.

## P5 Sketch
You can duplicate this [P5 Sketch ](https://editor.p5js.org/ueberf/sketches/SZgLRmIs-) to run it yourself, or create a new P5 environment and replace the code for the HTML and JavaScript file with the ones below: 

### Code for the index.html file
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/p5.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.4.0/addons/p5.sound.min.js"></script>
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/paho-mqtt/1.0.1/mqttws31.min.js" type="text/javascript"></script>

    <link rel="stylesheet" type="text/css" href="style.css">
    <meta charset="utf-8" />

  </head>
  <body>
    <main>
    </main>
    <script src="sketch.js"></script>
  </body>
</html>

```

### Code for the sketch.js file

```javascript
// MQTT setup
// MQTT client details:
let broker = {
    hostname: '[YOUR SHIFTR INSTANCE].cloud.shiftr.io',
    port: 443 
};

// MQTT client:
let client;
let creds = {
    clientID: 'color_picker',
    userName: '[YOUR SHIFTR USER NAME]',
    password: '[YOUR SHIFTR USER PASSWORD / TOKEN]'
}

let mqtt_topic = "color_picker"


let colorPicker;

let chosen_color
let previous_color

function setup() {
  createCanvas(400, 400);
  colorPicker = createColorPicker('#000000');
  colorPicker.position(0, height + 5);
  chosen_color = colorPicker.color().toString()
  previous_color = chosen_color;
  console.log(previous_color);
  
  // MQTT setup
  client = new Paho.MQTT.Client(broker.hostname, Number(broker.port), creds.clientID);
    client.connect(
        {
            onSuccess: onConnect,
            userName: creds.userName,
            password: creds.password,
            useSSL: true
        })
  frameRate(5)
  
}

function draw() {
  background(220);
  background(chosen_color);
  chosen_color = colorPicker.color().toString();
  
  if(chosen_color !== previous_color){
    console.log(chosen_color.toString())
    previous_color = chosen_color
    
    sendMqttMessage(mqtt_topic, chosen_color)
  }
}


function onConnect() {
  console.log("connected!")
}

function sendMqttMessage(topic, message) {
    if (client.isConnected()) {
        msg = new Paho.MQTT.Message(message);
        msg.destinationName = topic;
        client.send(msg);
    }
}
```

## CircuitPython code for the MQTT

```python
# --- Imports
import time
import board
import busio
import p9813
from digitalio import DigitalInOut
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT

import p9813

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
   global incoming_value
   """Method callled when a client's subscribed feed has a new
   value.
   :param str topic: The topic of the feed with a new value.
   :param str message: The new value
   """
   print("New message on topic {0}: {1}".format(topic, message))

   # New values are saved in this variable
   incoming_value = message

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

#MQTT_topic = "Perlin"
#MQTT_topic = "ISS/distance"
#MQTT_topic = "ISS/coordinates"
#MQTT_topic = "Coffeemachine"
MQTT_topic = "color_picker"

# We will use this value to save new incoming data
incoming_value = 0
previous_value = 0


# Set up LED
pin_clk = board.D13
pin_data = board.D10
num_leds = 1
leds = p9813.P9813(pin_clk, pin_data, num_leds)

## --- Functions

# --- Setup

# --- Setup
leds.fill((0, 0, 0))
leds.write()

# Connect the client to the MQTT broker.
print("Connecting to MQTT broker...")
mqtt_client.connect()

# --- Main loop
while True:
   # This try / except loop is used to continuously get new data from MQTT, and reset if anything goes wrong
   try:
      mqtt_client.loop()
   except (ValueError, RuntimeError) as e:
      print("Failed to get data, retrying\n", e)
      wifi.reset()
      mqtt_client.reconnect()
      continue


   # Add your own looping functions to do something with the data below this line

   # Let's print the incoming data in our Serial Monitor
   if incoming_value is not previous_value:
        print(incoming_value)
        # Create a temporary variable to store the string
        led_string = incoming_value

        # Reduce the string to only the needed values of RGB
        led_value = led_string.replace('rgba(', '').replace(',1)', '')

        # Turn it into a color array
        led_colors = led_value.split(',')

        # Assign the color value to individual variables
        red = int(led_colors[0])
        green = int(led_colors[1])
        blue = int(led_colors[2])

        # Update the LED color
        leds.fill((red, green, blue))
        leds.write()

        # Keep track of our color changes
        previous_value = incoming_value

   time.sleep(0.01)

```