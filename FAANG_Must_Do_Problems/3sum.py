class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for (i,n) in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                temp=n+nums[l]+nums[r]
                if temp==0:
                    res.append([n,nums[l],nums[r]])
                    l,r=l+1,r-1
                    while l<r and nums[l]==nums[l-1]: 
                        l += 1
                    while l<r and nums[r]==nums[r+1]: 
                        r -= 1
                elif temp<0: 
                    l += 1
                else: r -= 1
        return res