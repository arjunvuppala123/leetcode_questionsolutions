class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in memo:
                return [i,memo[remainder]]
            memo[nums[i]] = i
        return [-1,-1]