class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
#         transpose=[]
        
#         row=len(matrix)
#         col=len(matrix[0])
        
#         for c in range(col):
            
#             newrow=[]
            
#             for r in range(row):
                
#                 newrow.append(matrix[r][c])
                
#             transpose.append(newrow)
            
#         return transpose  
        
    
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
                
            