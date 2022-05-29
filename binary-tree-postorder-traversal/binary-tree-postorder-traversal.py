# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root: return root
        # def solve(root):
        #     if not root:
        #         return
        #     solve(root.left)
        #     solve(root.right)
        #     ans.append(root.val)
            
        def solve(root):
            visited=set()
            stack=[]
            
            node=root
            
            while stack or node:
                if node:
                    stack.append(node)
                    node=node.left
                else:
                    node=stack.pop()
                    if node.right and not node.right in visited :
                        stack.append(node)
                        node=node.right
                    else:
                        visited.add(node)
                        ans.append(node.val)
                        node=None
        solve(root)
        return ans