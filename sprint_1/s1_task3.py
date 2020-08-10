def isPalindrome(s):
    str_list = list(s)  # tranforming given string to list
    str_dict = {i:str_list.count(i) for i in str_list} # dictionary comprehension
    counter = 0   # number of string characters which appear in string an odd number of times
    for i in str_dict.values(): 
        if i % 2 != 0 :    
            counter += 1
        if counter > 1 : # if it is  >1 - this string can't be a palindrome
            return False
    return True
    
    
