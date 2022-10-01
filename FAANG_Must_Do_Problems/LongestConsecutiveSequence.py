class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums.sort()
        ctr = 1
        temp = 1
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    temp += 1
                else:
                    ctr = max(ctr,temp)
                    temp = 1
        return max(ctr,temp)