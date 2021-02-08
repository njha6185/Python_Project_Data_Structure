class node:
    def __init__(self,data):
        self.data =data
        self.next=None

class singlyLinkedList:
    def __init__(self):
        self.head=None
    
    def display(self):
        temp=self.head
        if temp is None:
            print("Empty Linked list!!")
        while(temp):
            print(temp.data)
            temp=temp.next
            
    def add_last(self,data):
        newnode = node(data)
        temp = self.head
        
        if temp is None:
            self.head=newnode
        else:
            while(temp.next):
                temp=temp.next
            temp.next=newnode
            
    def add_first(self,data):
        newnode = node(data)
        newnode.next=self.head
        self.head=newnode
        
    def add_at_position(self,data,pos):
        newnode=node(data)
        temp=self.head
        if temp is None:
            self.head=newnode
        elif pos <= 1:
            self.add_first(data)
        else:
            for i in range(1,pos-1):
                if temp is not None:
                    temp=temp.next
                else:
                    break
            newnode.next=temp.next
            temp.next=newnode
            
    def delete_first(self):
        if self.head is None:
            print("Empty Linked list, cannot delete")
        else:
            deltemp=self.head
            self.head=self.head.next
            a=deltemp.data
            del deltemp
            return a
        
    def delete_at_pos(self,pos):
        temp=self.head
        if temp is None:
            print("Empty Linked list, cannot delete")
        elif pos == 1:
            self.delete_first()
        elif pos == 1:
            print("0 position is invalid")
        else:
            for i in range(1,pos-1):
                if temp.next is None:
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
            while(temp):                
                self.delete_first()
                temp=temp.next
            print("All element Deleted")
            
class stack: #LIFO : LAST IN FIRST OUT
    def __init__(self):
        self.stack=singlyLinkedList()
        
    def push(self,data):
        self.stack.add_first(data)
#         self.stack.display()
    
    def pop(self):
        print(self.stack.delete_first())
#         self.stack.display()
        
    def isEmpty(self):
        if self.stack.head == None:
            return True
        else:
            return False
        
    def peek(self):
        temp=self.stack.head
        return temp.data
    
    def displayStack(self):
        print("Display start , Stack is: <========================>")
        self.stack.display()
        print("Display END , Stack is: <========================>")
        
class queue: #FIFO : First IN FIRST OUT
    def __init__(self):
        self.queue=singlyLinkedList()
        
    def push(self,data):
        self.queue.add_last(data)
#         self.stack.display()
    
    def pop(self):
        print(self.queue.delete_first())
#         self.stack.display()
        
    def isEmpty(self):
        if self.queue.head == None:
            return True
        else:
            return False
        
    def peek(self):
        temp=self.queue.head
        return temp.data
    
    def displayqueue(self):
        print("Display start , Queue is: <========================>")
        self.queue.display()
        print("Display END , Queue is: <========================>")        
        
             
if __name__ == '__main__':
    
    Objqueue = queue()
    print(Objqueue.isEmpty())
    
    Objqueue.push(10)
    Objqueue.push(12)
    Objqueue.push(13)
    Objqueue.displayqueue()
    print("Peek")
    print(Objqueue.peek())
    Objqueue.displayqueue()
    Objqueue.push(15)
    Objqueue.displayqueue()
    print("Pop")
    Objqueue.pop()
    Objqueue.displayqueue()
    Objqueue.push(19)
    Objqueue.push(20)
    print(Objqueue.isEmpty())
    Objqueue.displayqueue()
    
#     ObjStack = stack()
#     print(ObjStack.isEmpty())
#     
#     ObjStack.push(10)
#     ObjStack.push(12)
#     ObjStack.push(13)
#     ObjStack.displayStack()
#     print("Peek")
#     print(ObjStack.peek())
#     ObjStack.displayStack()
#     ObjStack.push(15)
#     ObjStack.displayStack()
#     print("Pop")
#     ObjStack.pop()
#     ObjStack.displayStack()
#     ObjStack.push(19)
#     ObjStack.push(20)
#     print(ObjStack.isEmpty())
#     ObjStack.displayStack()
    
#     lList=singlyLinkedList()
#     print("Add last 2 times for 1,2")
#     lList.add_last(1)
#     lList.add_last(2)
#     lList.display()
#     print("Add first 2 times for 4,3")
#     lList.add_first(4)
#     lList.add_first(3)
#     lList.display()
#     print("Add pos 4 times for 5,6,7,8 at 1,6,3,0")
#     lList.add_at_position(5,1)
#     lList.add_at_position(6,6)
#     lList.add_at_position(7,3)
#     lList.add_at_position(8,0) 
#     lList.display()
#     print("delete first 2 ")#5,3,7,4,1,2,6
#     lList.delete_first()
#     lList.display()
# #     print("After delete all ")#None
# #     lList.delete_all()
# #     lList.display()
#     print("delete at 3 ")#5,3,4,1,2,6
#     lList.delete_at_pos(0)
#     lList.display()
