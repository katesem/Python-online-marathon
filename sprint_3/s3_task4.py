def divisor(n):
    iter_lst = iter([i for i in range(1, n+1) if n % i == 0]) 
    while True: 
        try: 
            yield next(iter_lst)
        except StopIteration: 
            yield None
