#  here the idea is to find the good pairs in the array its an easy level problem I fucking cant solve it 

# I took the help of gpt and I got to know to solve this first I took the help of the hint which made me clear how to solve 
# this can be solved in 3 steps 


# count the number of freqencies that occur in the nums list which can be known by using the dictionary method 



class Solution(object):
    def numIdenticalPairs(self, nums):

        # step 1 - here we would be counting the number of freq of each number 

        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) +1
            
        cnt = 0

        # adding the formula for cnt which was provided in the hint 

        for n in freq.values():
            cnt+= n*(n-1)//2


        #  step 3 return the final result 


        return cnt
    



      


        """
        :type nums: List[int]
        :rtype: int
        """
        