#  we need to return the elements in such a way that the first element is the main element and the biggest element 
# 

# for this we are taking a hard and brute force appraoch 

# thinking about the edge cases we took the approach 

# if the length of the array is 1 then just return the number if k is an even number like if k = 2 then we can add and pop it no issue will come else -1 
# if k remains to be 0 just return the number top most element 
#  if k == 1 like only one move then return -1 but if the length is higher like there are 2 elements then if one move is said to be done then popping nums[0] remaining element 
# would be nums[1]  
# and now if k > length of the nums like the array is of 4 number and said the moves to be done is 5 then just return the highest element of the list coz at the end we have to keep the 
# highest elemnent on the top 

# now main is we need to have the max of max of numbers which are popped which are k-1 elements only if k is smaller than length of nums



class Solution(object):
    def maximumTop(self, nums, k):

        n = len(nums)

        if n== 1:
            return nums[0] if k%2 == 0 else -1

        if k == 0 :
            return nums[0]

        if k == 1 :
            return nums[1] if n > 1 else -1 
            
        if k > n :
            return max(nums)
            
        return max(max(nums[:k-1]) , nums[k] if  k<n  else float('-inf'))    
        
        