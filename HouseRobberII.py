class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        table1 = [0,nums[0]]
        for i in range(1,len(nums)):
            table1.append(max(table1[i],table1[i-1]+nums[i]))
        table2 = [0,nums[1]]
        for i in range(2,len(nums)):
            table2.append(max(table2[i-1],table2[i-2]+nums[i]))
        return max(table1[n-1],table2[n-1])