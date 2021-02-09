class node:
    def __init__(self,data):
        self.data =data
        self.next=None

class singlyCircularLinkedList:
    def __init__(self):
        self.head=None
    
    def display(self):
        temp=self.head
        if temp is None:
            print("Empty Linked list!!")
            return
        while True:
            print(temp.data)
            temp=temp.next
            if temp==self.head:
                break
        return
            
    def add_last(self,data):
        newnode = node(data)        
        temp = self.head
        
        if temp is None:
            self.head=newnode
            newnode.next=self.head
            return
        else:
            while temp.next!=self.head:
                temp=temp.next
            newnode.next=self.head
            temp.next=newnode
        return
            
    def add_first(self,data):
        newnode = node(data)        
        temp = self.head
        
        if temp is None:
            self.head=newnode
            newnode.next=self.head
            return
        else:
            while temp.next!=self.head:
                temp=temp.next
            newnode.next=self.head
            temp.next=newnode
        self.head=newnode
        return
        
        
    def add_at_position(self,data,pos):
        newnode=node(data)
        temp=self.head
        if temp is None:
            self.add_first(data)
        elif pos <= 1:
            self.add_first(data)
        else:
            for i in range(1,pos-1):
                if temp.next == self.head:
                    break
                else:
                    temp=temp.next
                    
            newnode.next=temp.next
            temp.next=newnode
            
    def delete_first(self):
        if self.head is None:
            print("Empty Linked list, cannot delete")
            return
        elif self.head.next==self.head:
            a=self.head.data
            del self.head
            self.head=None            
            return a
        else:
            deltemp=self.head
            temp=self.head
            while temp.next != self.head:
                temp=temp.next
            self.head=deltemp.next
            temp.next=self.head
            a=deltemp.data
            del deltemp
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
            for i in range(1,pos-1):
                if temp.next == self.head:
                    print("Invalid position")
                    return
                temp=temp.next
            deltemp=temp.next
            temp.next=temp.next.next
            a=deltemp.data
            del deltemp
            return a
                
    def delete_all(self):
        if self.head is None:
            print("Empty Linked list, cannot delete")            
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            while(self.head!=None):
                deltemp=self.head              
                self.head=deltemp.next
                del deltemp
#             while(self.head!=None):                
#                 self.delete_first()
#                 temp=temp.next
            print("All element Deleted")
            
class singlyCircularTailedLinkedList:
    def __init__(self):
        self.tail=None
    
    def display(self):
        temp=self.tail.next
        if temp is None:
            print("Empty Linked list!!")
            return
        while True:
            print(temp.data)
            temp=temp.next
            if temp==self.tail.next:
                break
        return
            
    def add_last(self,data):
        newnode = node(data)
        
        if self.tail is None:
            self.tail=newnode
            newnode.next=newnode
            return
        else:
            newnode.next=self.tail.next
            self.tail.next=newnode
            self.tail=newnode
        return
            
    def add_first(self,data):
        newnode = node(data)
        
        if self.tail is None:
            self.tail=newnode
            newnode.next=self.tail
            return
        else:            
            newnode.next=self.tail.next
            self.tail.next=newnode
            return
        
        
#     def add_at_position(self,data,pos):
#         newnode=node(data)
#         temp=self.tail.next
#         if temp is None:
#             self.add_first(data)
#         elif pos <= 1:
#             self.add_first(data)
#         else:
#             for i in range(1,pos-1):
#                 if temp.next == self.tail.next:
#                     break
#                 else:
#                     temp=temp.next
#                      
#             newnode.next=temp.next
#             temp.next=newnode
             
    def delete_first(self):
        if self.tail is None:
            print("Empty Linked list, cannot delete")
            return
        elif self.tail.next==self.tail:
            a=self.tail.data
            del self.tail
            self.tail=None            
            return a
        else:
            deltemp=self.tail.next
            self.tail.next=deltemp.next
            a=deltemp.data
            del deltemp
            return a
#         
#     def delete_at_pos(self,pos):
#         temp=self.head
#         if temp is None:
#             print("Empty Linked list, cannot delete")
#         elif pos == 1:
#             self.delete_first()
#         elif pos == 0:
#             print("0 position is invalid")
#         else:
#             for i in range(1,pos-1):
#                 if temp.next == self.head:
#                     print("Invalid position")
#                     return
#                 temp=temp.next
#             deltemp=temp.next
#             temp.next=temp.next.next
#             a=deltemp.data
#             del deltemp
#             return a
#                 
#     def delete_all(self):
#         if self.head is None:
#             print("Empty Linked list, cannot delete")            
#         else:
#             temp=self.head
#             self.head=temp.next
#             temp.next=None
#             while(self.head!=None):
#                 deltemp=self.head              
#                 self.head=deltemp.next
#                 del deltemp
# #             while(self.head!=None):                
# #                 self.delete_first()
# #                 temp=temp.next
#             print("All element Deleted")            
            
if __name__ == '__main__':
#     lList=singlyCircularLinkedList()
    lList=singlyCircularTailedLinkedList()
    print("Add last 2 times for 1,2")
    lList.add_last(1)
    lList.add_last(2)
    lList.display()
    print("Add first 2 times for 4,3") #3,4,1,2
    lList.add_first(4)
    lList.add_first(3)
    lList.display()
#     print("Add pos 4 times for 5,6,7,8 at 1,6,3,0")#
#     lList.add_at_position(5,1)
#     lList.add_at_position(6,6)
#     lList.add_at_position(7,3)
#     lList.add_at_position(8,0) 
#     lList.display() #5,3,7,4,1,2,6
#     print("delete first 2 ")#3,7,4,1,2,6
#     lList.delete_first()
#     lList.delete_first()
#     lList.display()
#     print("After delete all ")#None
#     lList.delete_all()
#     lList.display()
#     print("delete at 3 ")#5,3,4,1,2,6
#     lList.delete_at_pos(3)
#     lList.display()
    