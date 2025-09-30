class Solution(object):
    def numIdenticalPairs(self, nums):

        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) +1
            
        cnt = 0

        for n in freq.values():
            cnt+= n*(n-1)//2


        return cnt

      


        """
        :type nums: List[int]
        :rtype: int
        """
        