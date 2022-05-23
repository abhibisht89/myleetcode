# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        strr=""
        
        cur=head
        
        while cur:
            strr+=str(cur.val)
            cur=cur.next
        
        if strr==strr[::-1]:
            return True
        else:
            return False