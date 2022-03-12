class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        uniq_nums = list(set(nums))
        count = {}
        for i in uniq_nums:
            count[i] = nums.count(i)
        sorted_count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        res = list(sorted_count.keys())
        return res[0:k]