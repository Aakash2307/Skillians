# Given an integer array num sorted in non-decreasing order.

# You can perform the following operation any number of times:

# Choose two indices, i and j, where nums[i] < nums[j].
# Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
# Return the minimum length of nums after applying the operation zero or more times.



# Approach:
# 1. Since the array is sorted, the best way to pair elements is to try matching
#    smaller elements from the first half with larger elements from the second half.
#
# 2. To do this, we split the array into two parts using the middle index:
#    - left pointer starts from the beginning (smallest numbers).
#    - right pointer starts from the middle (larger numbers).
#
# 3. We then use a while loop:
#    - If nums[left] < nums[right], that means we found a valid pair.
#      → remove both (count += 2), move both pointers ahead.
#    - Else, if nums[left] >= nums[right], the right number is not big enough.
#      → move the right pointer ahead to try the next larger number.
#
# 4. Continue until one of the pointers goes out of range.
#
# 5. Finally, the answer is total length - count (the number of elements we could not remove).
#
# This greedy approach ensures we remove as many pairs as possible.




class Solution(object):
    def minLengthAfterRemovals(self, nums):

        n = len(nums)

        mid = n//2

        #  split the array 

        left = 0
        right = mid
        count = 0

        while left < mid and right < n:
            if nums[left] < nums[right]:
                count += 2
                left += 1
                right += 1
            else:
                right += 1

        return n - count


