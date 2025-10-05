# there is a list of sentences we need to output which sentence  has the max no of words in it 


class Solution(object):
    def mostWordsFound(self, sentences):

        max_words = 0

        for i in sentences:
            word_count = len(i.split(" "))
            max_words = max(max_words , word_count)

        return max_words

