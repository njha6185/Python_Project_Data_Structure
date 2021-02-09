from _overlapped import NULL

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
class doublyLinearLinkedList:
    def __init__(self):
        self.head=None
        
    def displayForward(self):
        temp=self.head
        if temp is None:
            print("Empty Linked list!!")
            return
        while(temp):
            print(temp.data)
            temp=temp.next
            
    def displayBackard(self):
        temp=self.head
        if temp is None:
            print("Empty Linked list!!")
            return
        while(temp.next):
            temp=temp.next
        
        while(temp):
            print(temp.data)
            temp=temp.prev
            
    def add_first(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
            
    def add_last(self, data):
        newnode=node(data)
        temp=self.head
        if self.head is None:
            self.head=newnode
            return
        else:
            while(temp.next):
                temp=temp.next
            newnode.prev=temp
            temp.next=newnode
            
    def add_at_postion(self,data,pos):
        newnode=node(data)
        temp=self.head
        if self.head is None:
            self.head=newnode
            return
        elif pos <= 1:
            self.add_first(data)
            return 
        else:
            for i in range(1,pos-1):
                if temp.next is not None:
                    temp=temp.next
                else:                    
                    break
            newnode.prev=temp
            newnode.next=temp.next
            if temp.next is not None:
                temp.next.prev=newnode
            temp.next=newnode
            
    def delete_first(self):
        if self.head is None:
            print("Empty Linked list, cannot delete")
        else:
            deltemp=self.head
            self.head=self.head.next
            a=deltemp.data
            del deltemp
            if self.head is not None:
                self.head.prev=None
            return a
        
    def delete_at_pos(self,pos):
        temp=self.head
        if temp is None:
            print("Empty Linked list, cannot delete")
        elif pos == 1:
            self.delete_first()
        elif pos == 0:
            print("0 position is invalid")
        else:
            for i in range(1,pos):
                if temp.next is None:
                    print("Invalid position")
                    return
                temp=temp.next
            deltemp=temp.next
            temp.prev.next=temp.next
            if temp.next is NULL:
                temp.next.prev=temp.prev
            a=deltemp.data
            del deltemp
            return a
        
            

if __name__ == '__main__':
#     lList=singlyCircularLinkedList()
    lList=doublyLinearLinkedList()
    print("Add last 2 times for 1,2")
    lList.add_last(1)
    lList.add_last(2)
    lList.displayForward()
    print("Add first 2 times for 4,3") #3,4,1,2
    lList.add_first(4)
    lList.add_first(3)
#     print("Display Backward")
#     lList.displayBackard()
    print("Display Forwarward")
    lList.displayForward()
    print("Add pos 4 times for 5,6,7,8 at 1,6,3,0")#
    lList.add_at_postion(5,1)
    lList.add_at_postion(6,6)
    lList.add_at_postion(7,9)
    lList.add_at_postion(8,0) 
    lList.displayForward() #5,3,7,4,1,2,6
    print("delete first 2 ")#3,7,4,1,2,6
    lList.delete_first()
    lList.delete_first()
    print("Display Forwarward")
    lList.displayForward()
#     print("After delete all ")#None
#     lList.delete_all()
#     lList.display()
#     print("delete at 3 ")#5,3,4,1,2,6
    lList.delete_at_pos(3)
    print("Display Forwarward")
    lList.displayForward()            
            