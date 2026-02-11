from datetime import date, datetime

def age_checker(date_of_birth):

    if not isinstance(date_of_birth, str):
        raise TypeError('Date must be in string format: YYYY-MM-DD')
    try: 
        dob = date.fromisoformat(date_of_birth)
    except:
        raise ValueError( 'Date must be in YYYY-MM-DD')
    
    today = datetime.now().date() 
    
    
    age = today.year - dob.year
  
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    if age < 16:
        return f'Access is denied: your current age is {age} and you must be 16'
    
    return "Access granted!"

