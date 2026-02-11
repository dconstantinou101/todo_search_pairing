from datetime import date, datetime

def age_checker(date_of_birth):

    dob = date.fromisoformat(date_of_birth)
    today = datetime.now().date() 
    
    #rounds down to nearest integer
    age = ((today - dob).days)//365
    print(age)
    if age < 16:
        return f'Access is denied: your current age is {age} and you must be 16'
    
    return "Access granted!"

""" def age_checker(date_of_birth):
    dob = date.fromisoformat(date_of_birth)
    today = datetime.now().date()

    age = today.year - dob.year
    print(age)
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    if age < 16: 
        return f"Access is denied: your current age is {age} and you must be 16"

    return "Access granted!" """