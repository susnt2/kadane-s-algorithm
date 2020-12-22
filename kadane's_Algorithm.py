def max_sequence(a): 
    curr_sum = maxi = 0
    
    for x in a:
        curr_sum += x
        
        if maxi < curr_sum :
            maxi = curr_sum
        if curr_sum < 0:
            curr_sum = 0
            
    return maxi
