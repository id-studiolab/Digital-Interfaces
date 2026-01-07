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

  [Lists and basic functions](#lists-and-basic-functions)

  [Add data to a list](#add-data-to-a-list)

  [Calculate a list average](#calculate-a-list-average)

  [Map a number x from one range to another](#map-a-number-from-one-range-to-another)

--- 

## Lists and basic functions

A list is a collection of ordered elements, and it looks like this:
```python
my_list = [3, 2, 1, 5, 4]
```
Lists can be manipulated using some basic functions, here below we show some very useful functions you can use while coding.
```python
my_list = [3, 2, 1, 5, 4]

# Length
length_of_list = len(my_list) # 5

# Sum
sum_of_list = sum(my_list) # 15

# Minimum
minimum_of_list = min(my_list) # 1

# Maximum
maximum_of_list = max(my_list) # 5

# Append: Adds an element at the end of a list
my_list.append(6) # my_list: [3, 2, 1, 5, 4, 6]

# Pop: Removes the last element of the list
my_list.pop()  # my_list: [3, 2, 1, 5, 4]    (The 6 we added before was removed)
```

Using these 5 basic functions here below we show how you can use them to create some useful helper functions.

{: .note }
If you're seeing an error that looks like this: `unsupported operand type(s) for +: 'int' and 'str'` then you probably need to convert your elements to numbers before adding them to your list: `my_list.append(int(my_variable))`

### Add data to a list

```python
#  lst: The list
#  x: Element we wish to add to the list
#  maxLength: How long we want our list to be at most.
def add_to_bounded_list(lst, x, maxLength): 
    lst.append(x)  # Add x to the end of the list
    while len(lst) > maxLength:  # While the list exceeds the maximum length
        lst.pop(0)  # Remove the first item
```

**Code example**

```python
import time
import random

## Create an empty list
data_collection = []

## When a list gets longer than this number, is starts to push first entries out and makes room for new data
maximum_number_of_entries = 10

## --- Functions

#  lst: The list
#  x: Element we wish to add to the list
#  maxLength: How long we want our list to be at most.
def add_to_bounded_list(lst, x, maxLength): 
    lst.append(x)  # Add x to the end of the list
    while len(lst) > maxLength:  # While the list exceeds the maximum length
        lst.pop(0)  # Remove the first item

# --- Main loop
while True:
    ## Generate a random integer between 0 and 1024
    random_number = random.randint(0,1024)
    
    ## Add random_number to our list, and remove first entries when the maximum capacity is reached
    add_to_bounded_list(data_collection, random_number, maximum_number_of_entries)
    
    print(f"The data list is: {data_collection}")
    time.sleep(1)
```

--- 

### Calculate a list average

```python
# lst: Calculate average of this list
def calculate_average(lst):
    return sum(lst) / len(lst) # To get the average of a list, we get the sum of the list (all numbers added together) and divide it by the length of the list (the amount of numbers in the list)
```

**Code example**

```python
import time

## Creating some  variables
data_collection = [150,52,32,10,212,50,100]
calculated_average = 0

## --- Functions
def calculate_average(lst):
    return sum(lst) / len(lst) # To get the average of a list, we get the sum of the list (all numbers added together) and divide it by the length of the list (the amount of numbers in the list)

# --- Main loop
while True:
    calculated_average = calculate_average(data_collection)
    print(f"List average: {calculated_average}")
    time.sleep(1)
```
--- 

## Map a number from one range to another

Often it happens that our data has a range from 0 up to 1000, but our component only accepts values between 0 and 255.
This mapping function comes very useful in those cases.

### Basic Function

```python
# To map a number from one range to another, we just need to apply some math to the number.
def map_to_range(x, inputMin, inputMax, outputMin, outputMax): 
    # Calculate the size of the input range.
    inputSize = inputMax - inputMin 

    # Same as previous but for the minimum and maximum we want to work towards.
    outputSize = outputMax - outputMin

    # Find how the output range scales compared to the input range.
    multiplier = outputSize / inputSize

    # If our number is at the minimum, we want it to be at 0. This makes multiplying easier.
    y = x - inputMin 

    # Multiply said number by our multiplier so we get the correct range. For example a range from 0,1 turns into 0,180 by multiplying by 180.
    z = y * multiplier 
    
    # We get the result by adding the minimum of the To to our previous result.
    result = z + outputMin 
    return result  
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
def map_to_range(x, inputMin, inputMax, outputMin, outputMax): 
    # Calculate the size of the input range.
    inputSize = inputMax - inputMin 

    # Same as previous but for the minimum and maximum we want to work towards.
    outputSize = outputMax - outputMin

    # Find how the output range scales compared to the input range.
    multiplier = outputSize / inputSize

    # If our number is at the minimum, we want it to be at 0. This makes multiplying easier.
    y = x - inputMin 

    # Multiply said number by our multiplier so we get the correct range. For example a range from 0,1 turns into 0,180 by multiplying by 180.
    z = y * multiplier 
    
    # We get the result by adding the minimum of the To to our previous result.
    result = z + outputMin 
    return result  

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
      
        print(f"Raw value: {raw_value} // Mapped value: {mapped_value} // Mapped integer: {mapped_int}")
        time.sleep(0.1)

    time.sleep(0.1)
```

--- 

[Go back](step-1){: .btn .btn-gray }  [Fallback solution](no_internet){: .btn .btn-blue }
