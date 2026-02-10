from datetime import datetime

def age_checker(date_of_birth):
    age = date_of_birth - datetime.now().date()
    #if date_of_birth < datetime.now().date():
    print("####age###", age)
        #return "Access granted!"