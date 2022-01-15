lookup = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1
        if n not in lookup:
            lookup[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return lookup[n]