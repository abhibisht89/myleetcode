# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.solve(root.left,root.right)
    
    def solve(self,l,r):
        if not l and not r:
            return True
        
        if not l or not r:
            return False
        
        if l.val==r.val:
            lans=self.solve(l.left,r.right)
            rans=self.solve(l.right,r.left)
            return lans and rans
        else:
            return False