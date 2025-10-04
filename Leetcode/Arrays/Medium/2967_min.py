class Solution(object):
    def minimumCost(self, nums):

        def ispalindrome(x):
            return str(x) == str(x)[::-1]

        nums.sort()
        n = len(nums)
        median = nums[n // 2]

        # Initialize costs with infinity
        lower_cost = upper_cost = float('inf')

        # If median itself is a palindrome, return cost immediately
        if ispalindrome(median):
            return sum(abs(num - median) for num in nums)

        # Search downward for nearest palindrome
        lower = median
        while lower > 0:
            if ispalindrome(lower):
                lower_cost = sum(abs(num - lower) for num in nums)
                break
            lower -= 1

        # Search upward for nearest palindrome
        upper = median
        while upper <= 10**9:
            if ispalindrome(upper):
                upper_cost = sum(abs(num - upper) for num in nums)
                break
            upper += 1

        return min(lower_cost, upper_cost)
