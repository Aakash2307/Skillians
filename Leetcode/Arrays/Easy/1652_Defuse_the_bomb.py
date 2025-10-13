"""
🧩 Problem: Defuse the Bomb (LeetCode 1652)

A circular array problem:
Each element in the array should be replaced by the sum of:
- The next k elements if k > 0
- The previous |k| elements if k < 0
- 0 if k == 0

---

💡 Example:
Input: code = [5, 7, 1, 4], k = 3
Output: [12, 10, 16, 13]

Explanation:
- For index 0 (5): next 3 elements → 7 + 1 + 4 = 12
- For index 1 (7): next 3 elements → 1 + 4 + 5 = 10
- For index 2 (1): next 3 elements → 4 + 5 + 7 = 16
- For index 3 (4): next 3 elements → 5 + 7 + 1 = 13

---

🔁 How wrapping works:
We use modulo `% n` to move circularly around the list.
For example, `(i + j) % n` wraps forward, `(i - j) % n` wraps backward.

---

🧠 Key Idea:
- Keep the original array unchanged while computing.
- Use a loop to sum the next or previous elements.
- Return a new result list.
"""


class Solution(object):
    def decrypt(self, code, k):

        n = len(code)

        result  = [0]*n

        if k == 0:
            return result

        for i in range(n):
            s = 0

            if k > 0 :
                for j in range(1, k+1):
                    s += code[(i+j) % n]

            else :
                for j in range (1 , abs(k)+1):
                    s += code[(i-j) % n]

            result[i] = s
        return result



