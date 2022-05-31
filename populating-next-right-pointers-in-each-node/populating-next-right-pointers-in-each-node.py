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
        if not root:return root
        q=[]
        q.append(root)
        while q:
            cur=q.pop()
            if cur.left and cur.right:
                cur.left.next=cur.right
                if cur.next:
                    cur.right.next=cur.next.left
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root         