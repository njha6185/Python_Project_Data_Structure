class graph:
    def __init__(self):
        self.mat=list(list())
    def graph(self,size):
        for i in range(size):
            temp=[]
            self.mat.append(temp)
    def accept(self):
#         print(self.mat)
        edge_cnt=int(input('Enter No of Edges'))
        for i in range(edge_cnt):
            from_d=int(input('Enter No of Edges from '))
            to_d=int(input('Enter No of Edges to'))
            self.mat[from_d].append(to_d)
            self.mat[to_d].append(from_d)
        
    def display(self):
        for i in self.mat:
            print(i)
    
    def dfs_Algo(self,start):
        stack=[]
        visited={}
        stack.push(start)
        visited[start]=True
        while(stack):
            trav=stack[-1]
            stack.pop()
            print(trav)
            for i in self.mat[trav]:
                if visited[i]==False:
                    stack.push(i)
                    visited[i]=True
                    
    def bfs_Algo(self,start):
        queue=[]
        visited={}
        queue.push(start)
        visited[start]=True
        while(queue):
            trav=queue[0]
            queue.pop(0)
            print(trav)
            for i in self.mat[trav]:
                if visited[i]==False:
                    queue.push(i)
                    visited[i]=True 
            
if __name__=='__main__':
    obj=graph()
    obj.graph(6)
    obj.accept()
    obj.display()            