
#  the main approach is to first declare 3 arrays of same length rightSum , leftSum , result 
# for leftsum array add numbers as it says from left and for rightsum start from behind
#  now we need to find the modulus for the difference of the left and rigt sum so we use the abs function and add it 
# to the result and move on 



class Solution(object):
    def leftRightDifference(self, nums):


        n = len(nums)
        rightSum = [0] *n
        leftSum = [0] * n
        result = [0] * n

        for i in range(1,n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]

        for i in range(n-2 , -1 , -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]

        for i in range(n):
            result[i] = abs(leftSum[i] - rightSum[i])

        return result