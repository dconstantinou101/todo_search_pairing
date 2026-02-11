# {{Age Checker}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.




## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._


```python


def age_checker(date_of_birth)
    """ checks a users age is above or below 16
    Parameters: (list all parameters and their types)
    entry: a string containing a date of birth in the format 'YYYY-MM-DD`

    Returns: (state the return value and its type)
    if age >= 16 return a string 'access granted' otherwise if age < 16 returns 'access is denied: your cuurent age is x and you must be 16'

    """

    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests


```python


"""
Given a birth year for an age greater than 16,
it returns access granted message

"""
age_checker("1960-10-21")
"Access granted!"


"""
Given a birth year for an age greater than 16,
it returns access denied message
"""
age_checker("2020-10-25")
'access is denied: your current age is x and you must be 16'

"""
Given a birth year for age of 16,
it returns access granted message

"""
age_checker("1960-10-21")
"Access granted!"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!# 


