# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head=cur=ListNode()
        carry=0
        
        while l1 or l2 or carry:
            v1=v2=0
            
            if l1:
                v1=l1.val
                l1=l1.next
            if l2:
                v2=l2.val
                l2=l2.next
            
            summ=v1+v2+carry
            carry=summ//10
            cur.next=ListNode(int(summ%10))
            cur=cur.next
        return head.next    
                