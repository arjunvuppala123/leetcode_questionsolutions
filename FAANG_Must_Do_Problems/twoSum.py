class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked={}
        for index , item in enumerate(nums):
            remaining = target - nums[index]
            if remaining in checked:
                return [index, checked[remaining]]
            checked[item] = index