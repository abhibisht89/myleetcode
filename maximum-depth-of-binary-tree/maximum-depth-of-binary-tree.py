# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # l=self.maxDepth(root.left)
        # r=self.maxDepth(root.right)
        # return max(l,r)+1
        q=[]
        q.append(root)
        
        def solve(root,level):
            if not root: return 0
            q=[]  
            q.append(root)
            while q:
                for _ in range(len(q)):
                    node=q.pop(0)
                    if node.left:
                        q.append(node.left)
                    if node .right:
                        q.append(node.right)
                level+=1       
            return level  
        return solve(root,0)        

                    
            
            
            
