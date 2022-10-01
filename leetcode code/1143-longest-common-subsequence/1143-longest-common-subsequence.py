class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows,cols = len(text1)+1,len(text2)+1
        dp = [0]*cols
        for i in range(1,rows):
            prev = 0
            for j in range(1,cols):
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j-1],dp[j])
                prev = temp
        return dp[-1]