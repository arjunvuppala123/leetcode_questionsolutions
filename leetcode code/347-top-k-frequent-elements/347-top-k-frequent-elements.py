class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        uniq_nums = list(set(nums))
        res = []
        
        for num in uniq_nums:
            my_dict[num] = nums.count(num)
        
        my_dict = dict(sorted(my_dict.items(),key = lambda x:x[1],reverse=True))
        
        for key in my_dict:
            if len(res) == k:
                return res
            res.append(key)
        
        return res