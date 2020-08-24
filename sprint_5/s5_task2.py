def divide_number(num_1, num_2):
    try:
        res = int(num_1)/ int(num_2)
    
    except ZeroDivisionError:
        print('Oops, division by zero is error!!! \nClosed all connections.')
    except ValueError as e:
        print('Value Error \nClosed all connections.')
    except :
        print('Something went wrong:( \nClosed all connections.')
    else:
        print(f'Result is {res}  \nNo exceptions:) \nClosed all connections.')
