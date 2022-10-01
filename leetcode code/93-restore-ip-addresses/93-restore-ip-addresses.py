class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []
        self.backtrack(s, [], 0)
        return self.res
    
    def backtrack(self, s, current, start):
        if len(current) == 4:
            if start == len(s):
                self.res.append(".".join(current))
            return
        for i in range(start, min(start+3, len(s))):
            if s[start] == '0' and i > start:
                continue
            if 0 <= int(s[start:i+1]) <= 255:
                self.backtrack(s, current + [s[start:i+1]], i + 1)