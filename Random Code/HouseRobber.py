class Solution:
    def rob(self, nums: List[int]) -> int:
        table = [0,nums[0]]
        for i in range(1,len(nums)):
            table.append(max(table[i],table[i-1]+nums[i]))
        return table[-1]