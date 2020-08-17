import re
import copy

def create_account(user_name, p1, s_w1):
    if not re.search("(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%&_*])(?=.*[A-Z])",p1) \
    or len(p1)< 6:
        raise ValueError
    
    def check(p2,s_w2):
        s_w = copy.deepcopy(s_w1) #vacant list for checking lists match
        for i in s_w2:
            if i in s_w:
                s_w.remove(i)
                      
        return (p1==p2 and len(s_w2) == len(s_w1) and len(s_w)<=1)
    return check
