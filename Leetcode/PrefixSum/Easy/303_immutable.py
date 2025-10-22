class NumArray(object):

    def __init__(self, nums):
        n = len(nums)
        for i in range(1 ,n):
            nums[i] += nums[i-1]


        self.nums = nums
        
        

    def sumRange(self, left, right):

       

        if left == 0 :
            return self.nums[right]

        

        return self.nums[right] - self.nums[left - 1]
       


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)