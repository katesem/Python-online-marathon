
def studying_hours(a):
    res = []   # stores maximum non-decreasing contiguous subarray
    res.append(a[0])
    max_len, temp_len = 0, 1  # store maximum length of subarray and current(temporary) length
    
    for i in range(1, len(a)):
        if a[i-1] <= a[i]:
            res.append(a[i-1])
            temp_len += 1
            
        else :
            if temp_len > max_len:
                max_len = temp_len
                
            res = []
            temp_len = 1
        
    if temp_len > max_len:
            max_len = temp_len
            
    return max_len
