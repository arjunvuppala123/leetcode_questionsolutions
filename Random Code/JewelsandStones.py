import re

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        total = 0
        for jewel in jewels:
            if jewel in stones:
                total += stones.count(jewel)
        return total