from collections import Counter

class Solution(object):
    def checkInclusion(self, s1, s2):
        n = len(s1)
        k = len(s2)

        if n>k :
            return False

        

        s1_count= Counter(s1)
        window_count = Counter(s2[:n])


        # Here we need to check the first window 

        if window_count == s1_count:
                return True

        for i in range(n,k):

            

            # we also need to update the window 

            window_count[s2[i]] +=1
            window_count[s2[i-n]] -= 1

            if window_count[s2[i - n]] == 0:
                del window_count[s2[i - n]]

            #  we need to do the same process again after we are shifting the window


            if window_count == s1_count:
                return True


           


        return False

        
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        