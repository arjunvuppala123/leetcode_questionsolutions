import sys

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n,ans,left,sum = len(nums),sys.maxsize,0,0
        for i in range(n):
            sum += nums[i]
            while sum>=target:
                ans = min(ans,i+1-left)
                sum -= nums[left]
                left += 1
        return ans if ans != sys.maxsize else 0