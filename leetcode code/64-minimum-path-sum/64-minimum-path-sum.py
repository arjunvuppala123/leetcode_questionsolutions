class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        
        cache = [[0 for i in range(cols)] for j in range(rows)]
        
        def dfs(grid,i,j):
            if i >= rows or j >= cols:
                return float("inf")
            if i == rows-1 and j == cols-1:
                return grid[i][j]
            if cache[i][j] == 0:
                cache[i][j] = grid[i][j] + min(dfs(grid,i+1,j),dfs(grid,i,j+1))
            
            return cache[i][j]
            
        return dfs(grid,0,0)