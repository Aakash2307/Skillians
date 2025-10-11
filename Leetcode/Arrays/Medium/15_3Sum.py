# LeetCode Problem: 15. 3Sum
# -----------------------------------------------------------
# Approach:
# 1. Sort the input array to easily handle duplicates and use two-pointer technique.
# 2. Iterate through each element 'nums[i]' as the first number of the triplet.
#    - Skip duplicates for 'nums[i]' to avoid repeating same triplets.
# 3. For each 'i', use two pointers:
#    - left = i + 1
#    - right = n - 1
#    Move these pointers inward based on the current total:
#       - If total < 0 → increment left (need a bigger sum)
#       - If total > 0 → decrement right (need a smaller sum)
#       - If total == 0 → found a valid triplet, add to result
# 4. After finding a valid triplet, move both pointers and skip duplicate values
#    for nums[left] and nums[right] to ensure unique triplets.
# 5. Continue until all combinations are checked.
#
# Time Complexity: O(n^2)  -> Sorting O(n log n) + two-pointer traversal O(n^2)
# Space Complexity: O(1)   -> Only uses result list (ignoring output)
#
# Example:
# Input: [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]

class Solution(object):
    def threeSum(self, nums):

        n = len(nums)
        nums.sort()
        result = []

        for i in range (n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = n-1

            while left < right :

                total = nums[i] + nums[left] + nums[right]

                if total < 0 :
                    left += 1

                elif total > 0 :
                    right -= 1

                else :
                    result.append([nums[i] , nums[left] , nums[right]])

                    left+=1
                    right -= 1


                    while left < right and nums[left] == nums[left - 1]:
                        left +=1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
                
                       
        