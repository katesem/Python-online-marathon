def logger(func):

    def wrapped(*args,**kwargs):
        if args and kwargs:
            op = list(args) + list(kwargs.values()) 
        else:
            op = list(kwargs.values()) if kwargs else list(args)
            
        if func.__name__ != 'print_arg':
            print(f'Executing of function {func.__name__} with arguments '\
                + (', ').join([str(x) for x in op]) + '...')
            return func(op)
        else:
            return(print(func(op)))
    return wrapped


@logger
def sum(op):
    s = 0
    for el in op:
        s += el
    return s
    
@logger
def print_arg(arg): 
    ans = (', ').join([str(x) for x in arg])
    print(ans)
    return('Executing of function print_arg with arguments ' + ans + '...') 
    
    
@logger
def concat(op):
    return ('').join([str(x) for x in op])
