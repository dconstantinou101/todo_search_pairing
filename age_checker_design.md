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
[1] Given a birth year for an age greater than 16,
it returns access granted message

"""
age_checker("1960-10-21")
=>"Access granted!"


"""
[2] Given a birth year for an age less than 16,
it returns access denied message
"""
age_checker("2010-07-10")
=>'access is denied: your current age is 15 and you must be 16'

"""
[3] Throws an error if date of birth is
not in the correct format'YYYY-MM-DD`

"""
age_checker(15)
=>ValueError 'Date must be in string format YYYY-MM-DD'

"""
[4] Throws an error when date of birth is
not a string

"""
age_checker('01-02-2010')
=>TypeError 'Date must be a string format: YYYY-MM-DD'

"""
[5] Given that today is the users birthday returns
access granted message

"""
birthdate = (todays_date - 16 years)
age_checker(birth_date.isoformat())
=> 'Access granted'
"""
[6] Given that tomorrow  the user will turn 16, it returns 
access denied message

"""
birthdate = (todays_date - 16 years) + 1 day
age_checker(birth_date.isoformat())
=> 'Access is denied: your current age is 15 and you must be 16'
"""
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE


```

Ensure all test function names are unique, otherwise pytest will ignore them!# 


