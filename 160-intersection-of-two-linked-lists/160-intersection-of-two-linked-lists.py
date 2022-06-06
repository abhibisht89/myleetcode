# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
#         mp={}
        
        if headA is None or headB is None:
            return None
        
#         cur=headA
#         while cur:
#             mp[cur]=1
#             cur=cur.next
            
#         cur=headB
        
#         while cur:
#             if cur in mp:
#                 return cur
#             else:
#                 mp[cur]=1
#             cur=cur.next 
        
        
        cura=headA
        
        while cura.next:
            cura=cura.next
        end=cura    
        cura.next=headB     

        
        def getcyclenode(head):
            if not head:
                return None

            slow=head
            fast=head
            iscycle=False


            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next

                if slow==fast:
                    iscycle=True
                    break

            if iscycle: 

                slow=head

                while slow!=fast:
                    slow=slow.next
                    fast=fast.next

                return slow 
            else:
                return None
            
        ansnode=getcyclenode(headA)  
        
        end.next=None
        
        return ansnode
        