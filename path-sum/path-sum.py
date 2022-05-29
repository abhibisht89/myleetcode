# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:        
        if not root:
            return False
        
        return self.solve(root,0,targetSum)
     
    def solve(self,node,summ,target):
        if not node:
            return False
        
        if node.left==None and node.right==None:
            summ+=node.val
            if summ==target:
                return True
            
        lans=self.solve(node.left,summ+node.val,target)
        rans=self.solve(node.right,summ+node.val,target)
            
        return lans or rans
            