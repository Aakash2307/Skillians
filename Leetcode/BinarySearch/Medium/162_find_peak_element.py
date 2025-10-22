
# in this we need to find the peak element where the element neighbours are smaller than them


# lets understand this with this an example
# nums = [1,2,1,3,5,6,4]

# lets learn through the code

class Solution(object):
    def findPeakElement(self, nums):

        n = len(nums)
        low = 0  #  now the low becomes 1
        high = n-1  # the high becomes 4

        while low < high :
            mid = (high+low)//2  # the mid no becomes 3 

            if nums[mid] < nums[mid+1]:  # here this condition runs where 3 is less than 5
                low = mid+1  # now the new low is no 5 


            # now when loop runs again the low is 5 and high is 4 and the new mid becomes 6 which is the peak element acc to the question
            # now when the peak element is found we need to return the index



            else:

                # else, peak is at mid or on the left
                high = mid


            # to return the index 6 no is present at index 6 but it should be 5 as it is a zero indexed array 
            # ṭo return that we would returning low which is the previous index of the peak element 
            # now we could why now mid-1 we could have return cause the mid changes again and again so it cannot be declared

        
        return low

            
        """
        :type nums: List[int]
        :rtype: int
        """
        