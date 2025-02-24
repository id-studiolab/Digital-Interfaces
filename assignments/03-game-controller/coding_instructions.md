---
layout: default
title: Code instructions
grand_parent: Assignments
parent: "3: Game Controller"
nav_order: 0
has_children: false
---

Coding can look like a super complicated skill to learn, but if we decompose each component and learn them individually it can turn out to be quite easy!

In this tutorial we will present 3 basic components, mainly:
- **Variables** -> Used for storing values
- **If-else statements** -> Used for decision making
- **While loops** -> Used to easily repeat operations

## Variables
A variable is like a box that stores information for your program. You can declare a variable and give it a value, and later change that value if needed.

```python
score = 5      # Declares a variable named "score" and assigns it a value of 5

score = 6      # Updates the value of "score" to 6
```

## If-Else statements

`if` , `elif` and `else` statements help your program choose between different actions based on conditions.

```python
current_state = 0

if buttun_pressed is True:
    current_state = 1
else:
    current_state = 0
```

In the previous example our code checks whether the button has been pressed, if that's the case then `current_state` will be updated to have value 1.

Here's how to use each statement:

- `if`: States the **First** condition, can be used on its own
- `else`: States the **Last** and fallback condition, must either follow an `if` or `elif`
- `elif`: States an alternative condition after an `if`, must either follow an `if` or `elif`

The main difference between `else` and `elif` is that `elif` can have condition parameters, while `else` cannot, for example:

```python
condition = False

if condition is True:
    print('Condition satisfied!')
elif button_is_pressed is True:
    print('Button is pressed!')
else:
    print('Idle')
```


## While loops
While loops are parts of code that are repeated, like the name suggests, **while** a certain condition is satisfied

```python
while button_is_pressed:
    print('Button is pressed!')        # Print while button is pressed
    button_is_pressed = button.value   # Detect button press
```

Keep in mind that only the code inside the `while` block will be executed as long as the 
condition is satisfied, thus it's important to update the variable checking the condition if we want to exit the loop at some point.

_Small note: writing `button_is_pressed is True` and `button_is_pressed` is essentially the same thing, although the first one makes it easier to understand the code while reading it._

The most common while loop you will see during this course is the `while True:` loop.
This loop defines the behavior that your code will keep repeating while it's on.

Remember to always include  `time.sleep(0.1)` at the end of your `while True:` loop, this prevents it to execute your code too fast and overwhelm the board.

```python
while True:

    # Your code logic here....

    time.sleep(0.1)
```