---
layout: default
title: "Step 2: Interpreting data for our embodiment"
parent: "Week 4: Data Embodiment"
grand_parent: Assignments
has_children: false
---

# Step 2: Interpreting data for our embodiment

Often we cannot use the pure data we receive from the MQTT server, but have to process it somehow to make it fit for our design. 

We created some helper functions and examples that you can use for this purpose:

  [Map a number x from one range to another](#map-a-number-x-from-one-range-to-another)

  [Add data to a list](#add-data-to-a-list)

  [Calculate a list average](#calculate-a-list-average)

  [Get the smallest number from a list](#get-the-smallest-number-from-a-list)

  [Get the largest number from a list](#get-the-largest-number-from-a-list)


--- 

## Map a number x from one range to another

### Basic Function

```python
# To map a number from one range to another, we just need to apply some math to the number.
def map_to_range(x, fromMin, fromMax, toMin, toMax):
    # Get the total "amount" of numbers between our minimum and maximum. For example if we want to go between 1 and 3, this will be 2.d
    fromTotal = fromMax - fromMin

    # Same as previous but for the minimum and maximum we want to work towards.
    toTotal = toMax - toMin

    # Divide the To by the From to see how much bigger (or smaller) the To is compared to the From.
    multiplier = toTotal / fromTotal

    # If our number is at the minimum, we want it to be at 0. This makes multiplying easier.
    y = x - fromMin

    # Multiply said number by our multiplier so we get the correct range. For example a range from 0,1 turns into 0,180 by multiplying by 180.
    z = y * multiplier

    # We get the result by adding the minimum of the To to our previous result.
    result = z + toMin
    return result  # Return
```

### Code Example
```python
import time

## Creating some empty variables
raw_value = 0
mapped_value = 0
mapped_int = 0

## --- Functions

# To map a number from one range to another, we just need to apply some math to the number.
def map_to_range(x, fromMin, fromMax, toMin, toMax): 
   # Get the total "amount" of numbers between our minimum and maximum. For example if we want to go between 1 and 3, this will be 2.d
   fromTotal = fromMax - fromMin 

   # Same as previous but for the minimum and maximum we want to work towards.
   toTotal = toMax - toMin

   # Divide the To by the From to see how much bigger (or smaller) the To is compared to the From.
   multiplier = toTotal / fromTotal

   # If our number is at the minimum, we want it to be at 0. This makes multiplying easier.
   y = x - fromMin 

   # Multiply said number by our multiplier so we get the correct range. For example a range from 0,1 turns into 0,180 by multiplying by 180.
   z = y * multiplier 
   
   # We get the result by adding the minimum of the To to our previous result.
   result = z + toMin 
   return result # Return 

# --- Setup

# --- Main loop
while True:
   
   # Count up from 0 to 1024
   for i in range(0, 1024, 1):
      raw_value = i
      
      # Map the raw_value that goes from 0 to 1024 to a new range of 0 to 255
      mapped_value = map_to_range(raw_value,0,1024,0,255)
      
      # Sometimes we only need the integer and not full float number
      # The int() function rounds our float input either up or down
      mapped_int = int(mapped_value)
      
      print("Raw value: {0} // Mapped value: {1} // Mapped integer: {2}".format(raw_value, mapped_value, mapped_int))
      time.sleep(0.1)

   time.sleep(0.1)
```

--- 

## Add data to a list

### Basic function

```python
def add_to_list(lst, x, length):  # x is the number we wish to add to the list, length is how long we want our list to be at most.
    lst.append(x)  # Add our x to the end of the list
    while len(lst) > length:  # While the list contains more than the allowed amount of items
        lst.pop(0)  # Remove the first item
```

### Code example

```python
import time
import random

## Create an empty list
data_collection = []

## When a list gets longer than this number, is starts to push first entries out and makes room for new data
maximum_number_of_entries = 10

## --- Functions
def add_to_list(lst, x, length): # x is the number we wish to add to the list, length is how long we want our list to be at most.
   lst.append(x) # Add our x to the end of the list
   while len(lst) > length: # While the list contains more than the allowed amount of items
      lst.pop(0) # Remove the first item

# --- Main loop
while True:
   ## Generate a random integer between 0 and 1024
   random_number = random.randint(0,1024)
   
   ## Add random_number to our list, and remove first entries when the maximum capacity is reached
   add_to_list(data_collection, random_number, maximum_number_of_entries)
   
   print("The data list is: {0}".format(data_collection))
   time.sleep(1)
```

--- 

## Calculate a list average

### Basic function

```python
def list_average(lst):
    return sum(lst) / len(lst) # To get the average of a list, we get the sum of the list (all numbers added together) and divide it by the length of the list (the amount of numbers in the list)
```

### Code example

```python
import time

## Creating some  variables
data_collection = [150,52,32,10,212,50,100]
calculated_average = 0

## --- Functions
def list_average(lst):
   return sum(lst) / len(lst) # To get the average of a list, we get the sum of the list (all numbers added together) and divide it by the length of the list (the amount of numbers in the list)

# --- Main loop
while True:
   calculated_average = list_average(data_collection)
   print("List average: {0}".format(calculated_average))
   time.sleep(1)
```
--- 

## Get the smallest number from a list

### Basic function

```python
def list_minimum(lst):
    return min(lst) # This is the function used to get the smallest number from a list
   
```

### Code example

```python
import time

## Creating some  variables
data_collection = [150, 52, 32, 10, 212, 50, 100]


## --- Functions
def list_minimum(lst):
    return min(lst)  # This is the function used to get the smallest number from a list


# --- Main loop
while True:
    print("List minimum: {0}".format(list_minimum(data_collection)))
    time.sleep(1)
```

## Get the largest number from a list

### Basic function

```python
def list_maximum(lst):
    return max(lst) # This is the function used to get the largest number from a list

```

### Code example

```python
import time

## Creating some  variables
data_collection = [150, 52, 32, 10, 212, 50, 100]


## --- Functions
def list_maximum(lst):
    return max(lst)  # This is the function used to get the largest number from a list


# --- Main loop
while True:
    print("List maximum: {0}".format(list_maximum(data_collection)))
    time.sleep(1)
```

[Previous Step](step-1){: .btn .btn-gray }  [Next Step](step-3){: .btn .btn-blue }
