"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head: return head
        
        copy=head
        while copy:
            newnode=ListNode(copy.val)
            newnode.next=copy.next
            copy.next=newnode
            copy=newnode.next
        
        
        copy=head
        while copy:
            copy.next.random=copy.random and copy.random.next
            copy=copy.next.next
        
        org=head
        copy=head.next
        cur=copy
        
        while cur:
            org.next=org.next and org.next.next
            cur.next=cur.next and cur.next.next
            cur=cur.next
            org=org.next
        return copy    
            
            
            
       
        
            