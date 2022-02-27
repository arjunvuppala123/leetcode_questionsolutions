class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        length = maxlength = 0
        for i in range(len(s)):
            if s[i] in used and length<= used[s[i]]:
                length = used[s[i]]+1
            else:
                maxlength = max(maxlength,i-length+1)
            used[s[i]] = i
            print(used)
        return maxlength