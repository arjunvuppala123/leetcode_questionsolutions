class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows,cols = n-1,n-1
        ctr = 1
        r,c = 0,0
        res = [[0 for i in range(n)] for j in range(n)]
        
        while r<=rows and c<=cols:
            for i in range(r,rows+1):
                res[r][i] = ctr
                ctr += 1
            for i in range(c+1,cols+1):
                res[i][cols] = ctr
                ctr += 1
            for i in range(rows-1,r-1,-1):
                res[cols][i] = ctr
                ctr += 1
            for i in range(cols-1,c,-1):
                res[i][c] = ctr
                ctr += 1
            
            r += 1
            c += 1
            rows -= 1
            cols -= 1
        
        return res
        
        
        
        
        
        