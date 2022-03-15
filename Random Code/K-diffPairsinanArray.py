class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        diff = {}
        answ = 0
        for x in nums:
            if x in diff:
                diff[x] += 1
            else:
                diff[x] = 1
        if k: # k>0
            answ=sum(x+k in diff for x in diff.keys())
        else: # k==0
            answ=sum(k>1 for k in diff.values())
                
        return answ