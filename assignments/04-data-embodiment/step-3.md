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

## Coffee Machine Fallback

1. Create a new file called `offline_coffee_machine_queue.py` , paste the code below into the file and save it on your `CIRCUITPY` device.
   ```python
   import random
   import math
   import time

   ## --- Variables 
   crowd_interval = 45.0 * 60.0 #minutes
   crowd_size = 10 # number of people arriving as crowd
   random_arrival_per_hour = 100

   last_check_time = 0.0
   current_time = time.monotonic()
   coffee_time = 15.0 #Decrease this number to have coffee be done quicker
   last_crowd_time = 0.0
   queue = 10
   helping_someone = 0
   coffee_count = 0

   # We will use this value to save new incoming data
   incoming_value = 0

   ## --- Functions
   def queue_management():
      global last_check_time
      global coffee_time
      global queue
      global last_crowd_time
      global crowd_size
      global crowd_interval
      global coffee_count

      current_time = time.monotonic()
      if current_time > last_crowd_time + float(crowd_interval):
         last_crowd_time = time.monotonic()
         queue = queue + crowd_size

      if random.random() <= crowd_size / 3600:
            queue = queue + 1

      if queue > 0:
         if current_time > last_check_time + float(coffee_time):
            last_check_time = time.monotonic()
            queue = queue - 1
            coffee_count = coffee_count + 1
            print("Someone just got coffee! Number of people in the queue:", queue)
            return True
      else:
         return False

   # --- Main loop
   while True:
      helping_someone = queue_management()
      incoming_value = coffee_count
      print("Total number of coffee's for the day:", incoming_value)
      time.sleep(1)
   ```

2. Add the following line to your `code.py` file and save it.
   ```python
   import offline_coffee_machine_queue
   ```

3. Open the `Serial Monitor` and you should see the collected data! 

---

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