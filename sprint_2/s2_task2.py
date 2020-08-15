def  morse_number(st):
    el = '-----'
    r = [el.replace('-','.',int(s)) if s <='5'else \
        el.replace('-','.', 10 - int(s))[::-1] for s in st]
    
    return (' ').join(r) 
    
