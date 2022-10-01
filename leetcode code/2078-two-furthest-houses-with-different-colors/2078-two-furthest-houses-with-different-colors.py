class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n,maxDistance = len(colors),0
        for i in range(n-1):
            for j in range(1,n):
                diff = abs(i-j)
                if ((colors[i] != colors[j]) and abs(i-j)>maxDistance):
                    maxDistance = diff
        return maxDistance