class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [matrix[i][j] for j in range(len(matrix[0])) for i in range(len(matrix))]
        
        if target in arr:
            return True
        else:
            return False
        