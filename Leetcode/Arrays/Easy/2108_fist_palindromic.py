class Solution(object):
    def firstPalindrome(self, words):

        n = len(words)

        for i in words:
            if i == i[::-1]:
                return i


        return ""

        

        """
        :type words: List[str]
        :rtype: str
        """
        