#recursive solution
class Solution:
    def fib(self, n: int) -> int:
        res = 0
        if n <= 1:
            return n
        else:
            return self.fib(n-2) + self.fib(n-1)
#iterative
class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        a=0
        b=1
        
        for i in range(n):
            a,b = b,a+b
        
        return a
#dynamic programming
lookup = {}
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n not in lookup:
            lookup[n] = self.fib(n-1) + self.fib(n-2)
        return lookup[n]