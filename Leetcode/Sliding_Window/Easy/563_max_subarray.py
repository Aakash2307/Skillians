# this is a sliding window problem where we need to calculate a fixed size 


class Solution(object):
    def findMaxAverage(self, nums, k):

        n = len(nums)  
        current_sum = sum(nums[:k])  

        maxSum = current_sum

        for i in range(k ,n):
            current_sum += nums[i] - nums[i-k]
            
            maxSum = max(maxSum , current_sum)

        return float(maxSum) / k




