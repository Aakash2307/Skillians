#  the problem states that we need to create a funciton where there are certain number of numbers in sorted array we need to find the 
# index of the value which we are given as a target if there is a number present then return the index 
# if there is no number which we are given as a target then we need to return the index where it could be input 


# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4


class Solution(object):
    def searchInsert(self, nums, target):

        n = len(nums)

        for i in range(0,n):
            if nums[i] >= target:
                return i 


        return n


#  this gives us a time complexity of O(n)


#  if we want we can go for a binary search solution tooo



class Solution(object):
    def searchInsert(self, nums, target):

        n = len(nums)

        left = 0 
        right = n - 1

        while (left < right ):

            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                right = mid + 1
            else :
                left = mid -1 

        return left
                