# nums = [1,2,4,7,9]


def binary_Search(target, nums):
    n = len(nums)

    low = 0
    high = n-1

    while low < high :
        mid = (low + high)// 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target :
            low = mid + 1
        else :
            high = mid - 1

    
    return -1



nums = [1,2,4,7,9]       

print(binary_Search(7,nums))
