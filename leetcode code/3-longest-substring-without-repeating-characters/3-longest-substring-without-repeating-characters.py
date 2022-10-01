class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n,ans,my_dict,i = len(s),0,{},0
        
        for j in range(n):
            if s[j] in my_dict:
                i = max(my_dict[s[j]],i)
            
            ans = max(ans,j-i+1)
            my_dict[s[j]] = j + 1
        
        return ans
        