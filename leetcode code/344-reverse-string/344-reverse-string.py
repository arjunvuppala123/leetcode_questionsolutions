class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0 
        while i <= len(s):
            s.insert(i, s.pop())
            i += 1
