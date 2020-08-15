import re

def pretty_message(s):
    return re.sub(r'(.|..|...)\1+', r'\1', s) 
    
# removing from the string repeated groups of symbols  which contain 1 or 2 or 3 characters
