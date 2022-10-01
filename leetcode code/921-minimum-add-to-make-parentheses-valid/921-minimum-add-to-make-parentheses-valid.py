class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = bal = 0
        for symbol in s:
            bal += 1 if symbol == '(' else -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal