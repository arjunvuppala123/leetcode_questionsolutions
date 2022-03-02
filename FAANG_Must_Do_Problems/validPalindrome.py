class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.lower() if char.isalnum()]
        new_str = s[::-1]
        return s==new_str