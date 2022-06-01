# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root: return root
        
        if root in [p,q]:
            return root
        
        lans=self.lowestCommonAncestor(root.left,p,q)
        rans=self.lowestCommonAncestor(root.right,p,q)
        
        if lans and rans:
            return root
        else:
            return lans or rans