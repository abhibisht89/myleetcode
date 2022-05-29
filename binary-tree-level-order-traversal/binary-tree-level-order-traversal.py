# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        
        ans=[]
        q=[]  
        q.append(root)
        
        while q:
            level=[]
            for _ in range(len(q)):
                node=q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node .right:
                    q.append(node.right)
            ans.append(level)       
        print(ans)
        return ans   
      
        
        
            