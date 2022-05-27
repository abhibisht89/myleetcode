# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next  or k==0: return head
        
        cur=head
        l=1
        while cur.next:
            cur=cur.next
            l+=1
            
        cur.next=head  
        
        for i in range(l - k % l):
            cur=cur.next
        
        head=cur.next
        cur.next=None
        return head
            