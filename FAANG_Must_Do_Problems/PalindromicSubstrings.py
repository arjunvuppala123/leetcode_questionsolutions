class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ctr = 0
        arr = []
        for i in range(n):
            for j in range(i,n):
                arr.append(s[i:j+1])
        for string in arr:
            if string == string[::-1]:
                ctr += 1
        return ctr