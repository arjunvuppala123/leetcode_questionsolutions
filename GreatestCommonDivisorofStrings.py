class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        
        
        if m==n:
            if str1==str2:
                return str1
            else:
                return ""
        
        elif m>n:
            if str1[:n] != str2:
                return ""
            else:
                return self.gcdOfStrings(str1[n:],str2)
        else:
            if str1 != str2[:m]:
                return ""
            else:
                return self.gcdOfStrings(str1,str2[m:])