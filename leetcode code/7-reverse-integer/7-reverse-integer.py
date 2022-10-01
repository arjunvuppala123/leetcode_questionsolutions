class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))
        rev = int(s[::-1])
        if rev > 2147483647:
            return 0
        return rev if x>0 else (rev*-1)