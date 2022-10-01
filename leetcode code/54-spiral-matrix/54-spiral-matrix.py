class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        def dfs(matrix,i,j,res):
            if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j] == '#':
                return
            res.append(matrix[i][j])
            matrix[i][j] = '#'
            if j+1>=i:
                dfs(matrix,i,j+1,res)
            dfs(matrix,i+1,j,res)
            dfs(matrix,i,j-1,res)
            dfs(matrix,i-1,j,res)
            
        dfs(matrix,0,0,res)
        return res