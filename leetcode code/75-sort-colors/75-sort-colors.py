class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        my_dict = {0:0, 1:0, 2:0}
        uniq_nums = list(set(nums))
        for num in uniq_nums:
            my_dict[num] = nums.count(num)
        res = my_dict[0]*[0] + [1]*my_dict[1] + [2]*my_dict[2]
        for i in range(len(nums)):
            nums[i] = res[i]