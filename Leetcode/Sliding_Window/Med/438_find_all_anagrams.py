from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        n, k = len(s), len(p)
        if n < k:
            return []

        p_count = Counter(p)
        window_count = Counter(s[:k])
        result = []

        # Slide the window
        for i in range(k, n):
            if window_count == p_count:
                result.append(i - k)  # append starting index

            # Update the window
            window_count[s[i]] += 1  # move one index forward from start
            window_count[s[i - k]] -= 1 # move one index forward from last
            if window_count[s[i - k]] == 0:
                del window_count[s[i - k]]

        # Check the last window after the loop
        if window_count == p_count:
            result.append(n - k)

        return result
