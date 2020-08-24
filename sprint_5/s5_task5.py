class MyError(Exception):
    pass

def check_positive(number):
    try:
        if float(number) < 0:
            raise MyError
        
    except MyError:
        print(f"You input negative number: {float(number)}. Try again.")
    except ValueError:
        print("Error type: ValueError!")
    else:
        print(f"You input positive number: {float(number)}")
