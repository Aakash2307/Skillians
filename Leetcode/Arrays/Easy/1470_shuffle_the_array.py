#  Here we need to have an arrya    

# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].


#  for this I have two approaches the first one is splitting the array into n equal length and then take each number and add it into the 
#  new result 
#  it looks like this 

def shuffle(nums, n):
    first = nums[:n]      # [x1, x2, ..., xn]
    second = nums[n:]     # [y1, y2, ..., yn]
    result = []
    for a, b in zip(first, second):
        result.append(a)
        result.append(b)
    return result


# SEcondly if I want I can also direct index it by not splitting them just add the number one from start and one from n+1 pos

# like this 

def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])     # xi
        result.append(nums[i+n])   # yi
    return result