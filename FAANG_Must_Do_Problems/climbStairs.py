fib = {}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in fib:
            return fib[n]
        if n==1 or n==0:
            return 1
        fib[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return fib[n]