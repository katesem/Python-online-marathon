def Cipher_Zeroes(s):
    
    points = 0
    for num in s:
        
        num = int(num)
        if num == 0 or num == 6 or num == 9:
            points += 1
            
        elif num == 8:
            points += 2
            
    if  points % 2 != 0:    # if number of points is odd
        points += 1
    
    elif  points % 2 == 0 and points != 0:
        points -= 1

    return str(bin(points))[2:]               # converting to binary and cut '0b' part of string
