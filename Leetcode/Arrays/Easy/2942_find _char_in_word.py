class Solution(object):
    def findWordsContaining(self, words, x):


        n = len(words)
        result = []

        for i , word in enumerate(words):
            if x in word:
                result.append(i)


        return result
                
