class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            
            while l<r:
                temp = nums[i] + nums[l] + nums[r]
                
                if temp < target:
                    res += (r-l)
                    l += 1
                else:
                    r -= 1
        
        return res