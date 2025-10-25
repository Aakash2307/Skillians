class Solution(object):
    def isPalindrome(self, s):

        # we need to clean the string and make it into lowercase and make it alphanumeric

        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        return s == s[::-1]
        """
        :type s: str
        :rtype: bool
        """