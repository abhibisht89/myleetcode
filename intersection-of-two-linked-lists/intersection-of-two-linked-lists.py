# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        mp={}
        
        if headA is None or headB is None:
            return None
        
        cur=headA
        while cur:
            mp[cur]=1
            cur=cur.next
            
        cur=headB
        
        while cur:
            if cur in mp:
                return cur
            else:
                mp[cur]=1
            cur=cur.next    
        