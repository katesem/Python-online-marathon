import re

def figure_perimetr(s):
    nums, p = [int(i) for i in re.findall(r'\d+', s)], 0
    nums[4:6], nums[6:] = nums[6:], nums[4:6] 
    calc = lambda l: ((l[2]-l[0])**2 + (l[3]-l[1])**2 )**0.5 
    
    for i in range(0,len(nums),2):
        p += calc(nums[i:i+4]) if i != 6 else calc(nums[:2] + nums[6:]) 
        
    return p  #perimeter
    
    
    #Test Example:
    
    #test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
    #print(figure_perimetr(test1))
