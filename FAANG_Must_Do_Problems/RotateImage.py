class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        res = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[n-1-j][i])
            res.append(temp)
        for i in range(len(matrix)):
            matrix[i] = res[i]