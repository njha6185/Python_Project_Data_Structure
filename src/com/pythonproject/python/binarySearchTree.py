class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        self.visited=False
        
class binarysearchTree:
    def __init__(self):
        self.root=None
        
    def add(self,data):
        newNode=node(data)
        trav=self.root
        if trav is None:
            self.root=newNode
#             print('Root addRecursiveWayed!! : ' + str(data))
            return
        while(1):
#             print('Data : ' + str(trav.data))
            if data < trav.data:
                if trav.left is None:
                    trav.left=newNode
#                     print('Data addRecursiveWayed in left!! : ' + str(data))
                    break
                trav=trav.left
            else:
                if trav.right is None:
                    trav.right=newNode
#                     print('Data addRecursiveWayed in Right!! : ' + str(data))
                    break
                trav=trav.right
                
    def binarysearch(self,data):
        trav=self.root
        while (trav):
            if trav.data == data:
                return 'Data Found : ' + str(trav.data)
            if data < trav.data:
                trav=trav.left
            else:
                trav=trav.right
        return 'No Data found'
    def addRecursive(self,data):
        if self.root is None:
            self.root=node(data)
#             print('Root addRecursiveWayed!! : ' + str(data))
            return
        else:
            self.addRecursiveWay(self.root,data)
    
    def addRecursiveWay(self,trav,data):
        if data < trav.data:
            if trav.left is None:
                trav.left=node(data)
                return
            self.addRecursiveWay(trav.left,data)
        else:
            if trav.right is None:
                trav.right=node(data)
                return
            self.addRecursiveWay(trav.right,data)
            
    def binarysearchRecursively(self,data):
#         print(self.root.data)
        if self.root is None:
            return 'Empty No data found'
        else:
            return self.binarysearchRecursivelyWay(self.root, data)        
    
    def binarysearchRecursivelyWay(self,trav,data):
#         print(trav.data)  
#         print('Hi'+ str(data))      
        if trav.data == data:
            return 'Data Found1 : ' + str(trav.data)
        if data < trav.data:
            return self.binarysearchRecursivelyWay(trav.left, data)
        else:
            return self.binarysearchRecursivelyWay(trav.right, data)
#         return 'No Data found' 
    def preOrder(self,trav):
        if trav is None:
            return
        print(trav.data)
        self.preOrder(trav.left)
        self.preOrder(trav.right)
    def preOrdercall(self):
        self.preOrder(self.root)
        
    def inOrder(self,trav):
        if trav is None:
            return        
        self.inOrder(trav.left)
        print(trav.data)
        self.inOrder(trav.right)
        
    def inOrdercall(self):
        self.inOrder(self.root)
        
    def postOrder(self,trav):
        if trav is None:
            return        
        self.postOrder(trav.left)        
        self.postOrder(trav.right)
        print(trav.data)
        
    def postOrdercall(self):
        self.postOrder(self.root)
        
    def delAll(self,trav):
        if trav is None:
            return        
        self.delAll(trav.left)        
        self.delAll(trav.right)
        print('data deleted  ' + str(trav.data))
        del trav
        
    def delAllCall(self):
        self.delAll(self.root)
        self.root = None
    
    def height(self,trav):
        if trav is None:
            return 0
        hL=self.height(trav.left)
        hR=self.height(trav.right)
        return max(hL,hR)+1
    def heightCall(self):
        return self.height(self.root)
    
    def preOredrNonRecursive(self):
        trav=self.root
        stack=[]
        if trav is None:
            return
        while(trav or stack):
            while trav is not None:
                print(trav.data)
                if trav.right is not None:
                    stack.append(trav.right)            
                trav=trav.left
            if (stack):
                trav=stack[-1]
                stack.pop()
                
    def inOredrNonRecursive(self):
        trav=self.root
        stack=[]
        if trav is None:
            return
        while(trav or stack):
            while(trav):
                stack.append(trav)
                trav=trav.left
            if stack:
                trav=stack[-1]
                stack.pop()
                print(trav.data)
                trav=trav.right
                
    def postOredrNonRecursive(self):
        trav=self.root
        stack=[]
        if trav is None:
            return
        while(trav or stack):
            while(trav):
                stack.append(trav)
                trav=trav.left
            if stack:
                trav=stack[-1]
                stack.pop()
                if trav.right is None or trav.right.visited==True:
                    print(trav.data)
                    trav.visited=True
                    trav=None
                else:
                    stack.append(trav)                
                    trav=trav.right
    def DFSAlgo(self,data): #Depth first search
        stack=[]
        stack.append(self.root)
        while stack:
            trav=stack[-1]
            stack.pop()
#             print(trav.data)
            if trav.data == data:
                return 'Data Found'
            if trav.right:
                stack.append(trav.right)
            if trav.left:
                stack.append(trav.left)
        return None
    
    def BFSAlgo(self,data): #Breadth first search
        queue=[]
        queue.append(self.root)
        while queue:
            trav=queue[0]
            queue.pop(0)
#             print(trav.data)
            if trav.data == data:
                return 'Data Found'
            if trav.left:
                queue.append(trav.left)
            if trav.right:
                queue.append(trav.right)
            
        return None
            
    def deleteSearchNodeBSt(self,data):
        trav=self.root
#         parent=self.root
        parent=None
        while (trav):
            if trav.data == data:
                return trav, parent
            if data < trav.data:
                parent=trav
                trav=trav.left
            else:
                parent=trav
                trav=trav.right
        parent=None
        return None,parent
    
    def deleteNode(self,data):
        temp, parent = self.deleteSearchNodeBSt(data)
        if temp is None:
            print("Node not found")
            return
#         if node has both child
        if temp.left is not None and temp.right is not None:
#             find its pred with pred's parent'
            parent = temp
            pred = temp.left
            while (pred.right):
                parent=pred
                pred=pred.right            
            
#             replace temp with predecaser
            temp.data=pred.data
#             consider pred node to be deleted
            temp=pred
#         if Node do not have right child
        if temp.right is None:
            if temp == self.root:
                self.root=temp.left
            elif temp.right is None:
                parent.left = temp.left
            else:
                parent.right=temp.left            
            del temp    
#         If Node do not have left child
        elif temp.left is None:            
            if temp == self.root:
                self.root=temp.right
            elif temp == parent.left:
                parent.left=temp.right
            else:
                parent.right=temp.right
            del temp
                
if __name__=='__main__':
    print('==========BST============')
    objBST=binarysearchTree()
    print(objBST.binarysearchRecursively(60))
    objBST.addRecursive(50)
    objBST.addRecursive(10)
    objBST.addRecursive(40)
    objBST.addRecursive(60)
    objBST.addRecursive(80)
    objBST.addRecursive(20)
    objBST.addRecursive(70)
    objBST.addRecursive(80)
    objBST.addRecursive(25)
    print('Data addRecursiveWayed')
    c=objBST.binarysearchRecursively(50)
    print(c)
    print(objBST.binarysearchRecursively(60))
    print(objBST.binarysearchRecursively(20))
    print(objBST.binarysearchRecursively(25))
    print('preOrder')
    objBST.preOrdercall()
    print('InOrder')
    objBST.inOrdercall()
    print('PostOrder')
    objBST.postOrdercall()
#     print('DelALL')
#     objBST.delAllCall()
    print('InOrder')
    objBST.inOrdercall()
    print('HEIGHT')
    print(objBST.heightCall())
     
    print('preOrderNonRecursive')
    objBST.preOredrNonRecursive()
    
    print('InOrderNonRecursive')
    objBST.inOredrNonRecursive()
    
    print('postOredrNonRecursive')
    objBST.postOredrNonRecursive()
    
    print('DFSAlgo')
    print(objBST.DFSAlgo(50))
    
    print('BFSAlgo')
    print(objBST.BFSAlgo(50))
    
    print('DeleteNODEBST')
    temp,parent=objBST.deleteSearchNodeBSt(20)
    print(temp.data)
    print(parent.data)