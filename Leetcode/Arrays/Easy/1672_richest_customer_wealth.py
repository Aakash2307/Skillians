# given an array which consisted of many subarray we need to find the sum of each subarray and find out which is the max sum of each array 



class Solution(object):
    def maximumWealth(self, accounts):
        result = []
        n = len(accounts)

        for i in accounts:
            result.append(sum(i))

        
        return max(result)
            
