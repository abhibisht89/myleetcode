# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=cur=ListNode()
        
        while list1 and list2:
            if list1.val<list2.val:
                newnode=ListNode(list1.val)
                cur.next=newnode
                # cur=newnode
                list1=list1.next
            else:
                newnode=ListNode(list2.val)
                cur.next=newnode
                # cur=newnode
                list2=list2.next
            cur=newnode
        cur.next=list1 or list2        
        return head.next         
                
        