class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        temp = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left,right = i+1,len(nums)-1
            while left<right:
                dummy = nums[i] + nums[left] + nums[right]
                if dummy == target:
                    return dummy
                if abs(dummy-target) < abs(temp-target):
                    temp = dummy
                if dummy<target:
                    left+=1
                else:
                    right-=1
        return temp
                