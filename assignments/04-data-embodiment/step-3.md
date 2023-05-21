---
layout: default
title: "Step 3 (optional): Working with an offline fallback"
parent: "Week 4: Data Embodiment"
grand_parent: Assignments
has_children: false
---

# Step 3 (optional): Working with an offline fallback

Designing with incoming live data is exciting, however it also makes our design susceptible for failures. What if the internet connection is disturbed? What if the server stops sending? 

It can also happen that something goes wrong during our workshop, or that you have issues with connecting your ItsyBitsy to the internet. For this case, we created some offline fallbacks that allow you to learn how to embody data even if you do not manage to connect, or if you do this workshop at a different time.

## ISS Distance and Perlin Noise Fallback

We saved some real data for the ISS and Perlin noise in these `.txt` files. This allows you to loop through the file and read the data as if it was coming from our MQTT server.

1. Download these two files by right-clicking and selecting `"Download linked file"` (or the equivalent of your browser):

   [Perlin_data.txt](Perlin_data.txt)

   [ISS_distance.txt](ISS_distance.txt)

2. Add the files `Perlin_data.txt` and `ISS_distance.txt` to your `CIRCUITPY` device.
3. Create a new file called `offline_data_handler.py` , paste the code below into the file and save it on your `CIRCUITPY` device.

   ```python
   import storage
   import time
   import random

   ## --- Variables 
   interval = 1.0 # time between data points in seconds

   ## Choose only one file at a time
   datasource = "ISS_distance.txt"
   #datasource = "Perlin_data.txt"

   last_check_time = 0.0

   file = open(datasource, "r")
   data = file.readlines()
   file.close()
   line_number = random.randint(0,len(data))

   datapoint = 0

   # We will use this value to save new incoming data
   incoming_value = 0

   ## --- Functions

   def get_data_point():
      global datapoint
      global last_check_time
      global data
      global line_number
      current_time = time.monotonic()

      if current_time > last_check_time + float(interval):
         line_number = line_number + 1
         datapoint = data[line_number]

      if line_number >= len(data) - 1 :
         line_number = 0

      return datapoint
      

   # --- Main loop
   while True:
      time.sleep(interval)
      
      incoming_value = get_data_point()
      print(incoming_value)
   ```

4. Add the following line to your `code.py` file and save it.

   ```python
   import offline_data_handler
   ```

5. Open the `Serial Monitor` and you should see the collected data!

[Previous Step](step-2){: .btn .btn-gray }
