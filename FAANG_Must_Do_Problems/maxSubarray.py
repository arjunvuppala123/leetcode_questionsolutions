class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if n==0:
            return -1
        dp = nums
        for i in range(1,n):
            dp[i] = max(dp[i],nums[i]+dp[i-1])
        return max(nums)
    