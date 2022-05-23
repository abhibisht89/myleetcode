# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         strr=""
        
#         cur=head
        
#         while cur:
#             strr+=str(cur.val)
#             cur=cur.next
        
#         if strr==strr[::-1]:
#             return True
#         else:
#             return False
        
        slow=fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        prev=None
        cur=slow
        
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        
        cur=head
        
        while cur!=slow:
            if prev.val!=cur.val:
                return False
            prev=prev.next
            cur=cur.next
        return True    
        
        