# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        
        # def solve(root):
        #     if not root:
        #         return root
        #     ans.append(root.val)
        #     solve(root.left)
        #     solve(root.right)
        # solve(root)
        # return ans
        
        ans=[]
        stack=[]
        stack.append(root)
        
        def solve(root):
            while stack:
                node=stack.pop(-1)
                ans.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:    
                    stack.append(node.left)
        solve(root)
        return ans
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            