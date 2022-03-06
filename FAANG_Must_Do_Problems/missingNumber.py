class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        observed_sum = sum(nums)
        actual_sum = 0
        for i in range(1,len(nums)+1):
            actual_sum += i
        return actual_sum - observed_sum