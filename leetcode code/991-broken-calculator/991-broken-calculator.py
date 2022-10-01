class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ctr = 0
        while startValue < target:
            ctr += 1
            if target%2:
                target += 1
            else:
                target //= 2
        return ctr+startValue - target