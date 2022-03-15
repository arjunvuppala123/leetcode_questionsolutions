class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j,k = i+1,len(nums)-1
            while j<k:
                dummy = nums[i]+nums[j]+nums[k]
                if dummy == target:
                    return dummy
                if abs(dummy-target)<abs(result-target):
                    result = dummy
                if dummy < target:
                    j += 1
                elif dummy > target:
                    k -= 1
        return result