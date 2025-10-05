class Solution(object):
    def runningSum(self, nums):
        result = []
        curr_sum = 0
        for i in nums:

            curr_sum += i
            result.append(curr_sum)


        return result

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        