class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,column = len(grid),len(grid[0])
        count = 0
        
        def dfs(i,j):
            if i<0 or i>=rows or j<0 or j>=column or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        for i in range(rows):
            for j in range(column):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count