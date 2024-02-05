# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def task_tracker(text):
    pass # Test-driving means _not_ writing any code here yet.

    # input type(text) = str
    # return value is boolean (True/False)
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string
Will return False
"""
task_tracker("") => False

"""
Given a string which contains #TODO 
Will return True
"""
task_tracker("#TODO dasnufnuobwa") => True

"""
Given long string which icludes #TODO embedded in the string
Returns True
"""
extract_uppercase("bfuionawouibfwoiau#TODOfjabewgbfu") => True
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
Ensure all test function names are unique, otherwise pytest will ignore them!
