class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        total = 0

        for i , num in enumerate(nums):
            if bin(i).count('1') == k :                 # count the set bits
                total += num
                

        return total    