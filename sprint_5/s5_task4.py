class ToSmallNumberGroupError(Exception):
    pass

def check_number_group(num):
    try:
        if int(num) < 10:
            raise ToSmallNumberGroupError
    except ToSmallNumberGroupError:
        print("We obtain error: Number of your group can't be less than 10")
    except ValueError:
        print("You entered incorrect data. Please try again.")
    else:
        print(f'Number of your group {num} is valid')
