class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = defaultdict(int)
        ctr = 0
        for t in time:
            ctr += hashmap[(60-t%60)%60]
            hashmap[t%60] += 1
        return ctr