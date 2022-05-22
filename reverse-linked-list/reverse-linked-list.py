# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#class

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        cur=head
        prev=None
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
            
        
