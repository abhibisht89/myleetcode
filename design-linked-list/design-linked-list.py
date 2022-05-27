class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        
    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        
        cur=self.head
        for _ in range(index):
            cur=cur.next
        return cur.val    
   

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)
    
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return
        
        cur=self.head
        nnode=ListNode(val)
        
        if index==0:
            nnode.next=self.head
            self.head=nnode
        else:
            for _ in range(index-1):
                cur=cur.next
            nnode.next=cur.next
            cur.next=nnode
        self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size: return
        cur=self.head
        
        if index==0:
            self.head=self.head.next
        else:
            for i in range(index-1):
                cur=cur.next
            cur.next=cur.next.next
        self.size-=1    
            
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)