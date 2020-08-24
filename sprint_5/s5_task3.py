def check_odd_even (number):
    try:
        res = number%2
    except TypeError:
        print('You entered incorrect data. Please try again.')
    else:
        print('Entered number is even'if res == 0 else'Entered number is odd')
