class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)
        
        if (p_len > s_len): return []
    
        p_freq = [0] * 26
        s_freq = [0] * 26
        sol = []
        
        for i in range(p_len):
            p_freq[ord(p[i]) - ord('a')] += 1
            s_freq[ord(s[i]) - ord('a')] += 1
           
        if p_freq == s_freq: sol.append(0)
            
        for i in range(1, s_len - p_len + 1):
            s_freq[ord(s[i - 1]) - ord('a')] -= 1;
            s_freq[ord(s[i + p_len - 1]) - ord('a')] += 1;
            if p_freq == s_freq: sol.append(i)
        
        return sol;