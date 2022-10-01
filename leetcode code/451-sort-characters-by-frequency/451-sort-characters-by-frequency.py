class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        result = [char for char in s]
        uniq_chars = list(set(result))
        count = {}
        
        for char in uniq_chars:
            count[char] = result.count(char)
        
        count = dict(sorted(count.items(),key = lambda x:x[1],reverse=True))
        
        for key in count:
            res += key*count[key]
        
        return res