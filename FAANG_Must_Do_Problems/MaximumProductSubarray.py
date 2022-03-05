class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = nums[::-1]
        for i in range(1,len(nums)):
            if nums[i-1] != 0:
                nums[i] *= nums[i-1] 
            if arr[i-1] != 0:
                arr[i] *= arr[i-1]
        return max(arr+nums)