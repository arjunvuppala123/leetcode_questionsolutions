class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i,j in zip(index,nums):
            res.insert(i,j)
        return res