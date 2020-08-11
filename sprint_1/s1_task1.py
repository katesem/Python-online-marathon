def kthTerm(n, k):
    b = (str(bin(k))[2:])    # converting to binary and cut '0b' part
    s = b[b.index('1'):]     # getting a slice
    res = 0
    s = s[::-1]
    
    for i in range(0,len(s)):
        if s[i] == '1':
            res += (n**i)
        
    return res
