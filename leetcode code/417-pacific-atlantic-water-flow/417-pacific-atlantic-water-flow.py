class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows,columns = len(heights),len(heights[0])
        pacific,atlantic = set(),set()
        res = []
        
        def dfs(i,j,my_set,prevHeight):
            if (i,j) in my_set or i<0 or i==rows or j<0 or j==columns or prevHeight>heights[i][j]:
                return
            my_set.add((i,j))
            dfs(i+1,j,my_set,heights[i][j])
            dfs(i-1,j,my_set,heights[i][j])
            dfs(i,j+1,my_set,heights[i][j])
            dfs(i,j-1,my_set,heights[i][j])
            
            
        
        for c in range(columns):
            dfs(0,c,pacific,heights[0][c])
            dfs(rows-1,c,atlantic,heights[rows-1][c])
        
        for r in range(rows):
            dfs(r,0,pacific,heights[r][0])
            dfs(r,columns-1,atlantic,heights[r][columns-1])
            
        for r in range(rows):
            for c in range(columns):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
            
        