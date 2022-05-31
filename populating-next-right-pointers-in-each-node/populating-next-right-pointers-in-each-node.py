"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ans=[]
        if not root:
            return root
        
        def solve(root):
            q=[]
            q.append(root)
            while q:
                curr=q.pop()
                if curr.left and curr.right:
                    curr.left.next = curr.right
                    if curr.next:
                        curr.right.next = curr.next.left
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)  
            return root  
        return solve(root)