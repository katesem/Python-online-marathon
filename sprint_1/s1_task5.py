#solution of this task based on Stack data structure and operations with it

def toPostFixExpression(e):
    prec = {}                    # stores operator priorities, where 3 - the highest priority, 1 - the lowest
    prec["*"] = 3  
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    stack = []        # for keeping operators.
    output = []       # list for output.
    
    for el in e:
        if el.isdigit():
            output.append(el)           # appending  to the end of the output list.
        
        elif el  == '(':
            stack.insert(0,el)
            
        elif el == ')':
            top_element = stack[0]           # imitation of Stack method pop()
            del stack[0]
            
            while top_element != '(':
                output.append(top_element)  
                top_element = stack[0]     
                del stack[0]
                
        else:
            while len(stack) > 0  and prec[stack[0]] >= prec[el]:           # if stack is not empty and priority of first stack element higher
                output.append(stack[0])
                del stack[0]
            stack.insert(0,el)
                
    while len(stack) > 0:       # if stack is not empty
        output.append(stack[0])
        del stack[0]
            
    return output
