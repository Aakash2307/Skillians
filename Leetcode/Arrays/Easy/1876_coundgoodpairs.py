# so here is the case right now we nee to count the substring of a string with length 3 with all unique values 






class Solution(object):
    def countGoodSubstrings(self, s):

        count  = 0 

        for i in range(len(s)):
            substring = s[i:i+3]

            if len(set(substring)) == 3 :
                count += 1

        
        return count
        """
        :type s: str
        :rtype: int
        """
        