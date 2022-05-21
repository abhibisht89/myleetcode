# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        cur=head
        
        for i in range(n):
            cur=cur.next
            
        if not cur:
            return head.next
        
        ptr=head
        
        while cur.next:
            cur=cur.next
            ptr=ptr.next
        
        ptr.next=ptr.next.next
        
        return head
        
        
        