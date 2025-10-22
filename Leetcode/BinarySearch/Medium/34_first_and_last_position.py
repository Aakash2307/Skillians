class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        n = len(nums)
        

        def findFirst(nums , target):
            high = n - 1
            low = 0

            first = -1


            while low <= high :
                mid = (high + low) // 2

                if nums[mid] == target:
                    first = mid
                    high = mid - 1

                elif nums[mid] < target:
                    low = mid + 1

                else : 
                    high = mid -1

                
            return first 


        
        def findLast(nums , target):
            high = n - 1
            low = 0

            last = -1

            while low <= high :
                mid = (high + low) // 2

                if nums[mid] == target :
                    last = mid
                    low = mid +1

                elif nums[mid] < target :
                    low = mid+1
                else :
                    high = mid-1

            
            return last



        return [findFirst(nums,target) , findLast(nums,target)]



