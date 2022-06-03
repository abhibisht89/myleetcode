class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row=len(matrix)
        col=len(matrix[0])
        
        self.dp=[[0 for _ in range(col+1)] for _ in range((row+1))]
        
        # for r in range(row):
        #     for c in range(col):
        #         self.dp[r+1][c+1]=self.dp[r+1][c]+ self.dp[r][c+1]+matrix[r][c]-self.dp[r][c]
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     summ=0
    #     for row in range(row1,row2+1):
    #         for col in range(col1,col2+1):
    #             summ+=self.data[row][col]
    #     return summ 
        
        for r in range(row):
            prefix=0
            for c in range(col):
                prefix+=matrix[r][c]
                above=self.dp[r][c+1]
                self.dp[r+1][c+1]=prefix+above
                     
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1]-self.dp[row1][col2+1]-self.dp[row2+1][col1]+self.dp[row1][col1]
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)