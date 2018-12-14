class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return
        m, n = len(matrix), len(matrix[0])
        self.memo = [[0 for j in range(n+1)] for i in range(m+1)]
        self.memo[1][1] = matrix[0][0]
        for j in range(2, n+1):
            self.memo[1][j] = matrix[0][j-1] + self.memo[1][j-1]
        for i in range(2, m+1):
            self.memo[i][1] = matrix[i-1][0] + self.memo[i-1][1]
        for i in range(2, m+1):
            for j in range(2, n+1):
                self.memo[i][j] = self.memo[i][j-1] + self.memo[i-1][j] - self.memo[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.memo[row2+1][col2+1] - self.memo[row1][col2+1] - self.memo[row2+1][col1] + self.memo[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
