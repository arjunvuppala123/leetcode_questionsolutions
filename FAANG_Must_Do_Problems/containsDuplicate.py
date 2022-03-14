class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()
        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                return True
        return False