class Solution(object):
    def removeDuplicates(self, nums):

        if not  nums:
            return 0 

        un_index = 0

        for i in range(0 , len(nums)):
            if nums[i] != nums[un_index]:
                un_index += 1
                nums[un_index] = nums[i]

        return un_index + 1

        """
        :type nums: List[int]
        :rtype: int
        """
        