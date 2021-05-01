class graph:
    def __init__(self):
        self.mat=list(list())
    def graph(self):
        for i in range(6):
            temp=[]
            for j in range(6):
                temp.append(0)
            self.mat.append(temp)
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
            for i in range(6):
                if self.mat[trav][i] != 0 and visited[i]==False:
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
            for i in range(6):
                if self.mat[trav][i] != 0 and visited[i]==False:
                    queue.push(i)
                    visited[i]=True 
                
            
    def isConnecrtedGraph(self,start):
        stack=[]
        
        visited={}
        stack.push(start)
        visited[start]=True
        count=1
        while(stack):
            trav=stack[-1]
            stack.pop()
            print(trav)
            for i in self.mat[trav]:
                if visited[i]==False:
                    stack.push(i)
                    visited[i]=True
                    count=count+1
                    if count == 6:
                        return True        
        return False
    def DFSsPANNINGtREE(self,start):
        stack=[]
        
        visited={False*6}
        stack.push(start)
        visited[start]=True
#         count=1
        while(stack):
            trav=stack[-1]
            stack.pop()
            
            for i in self.mat[trav]:
                if visited[i]==False:
                    stack.push(i)
                    visited[i]=True
                    print(trav+'-->'+i)        
#         return False    

    def bfs_singlePathLength(self,start):
        queue=[]
        visited={False*6}
        distance={0*6}
        distance[start]=0
        queue.push(start)
        visited[start]=True        
        while(queue):
            trav=queue[0]
            queue.pop(0)            
            for i in range(6):
                if self.mat[trav][i] != 0 and visited[i]==False:
                    queue.push(i)
                    visited[i]=True
                    distance[i]=distance[trav]+1     
        
    def isbipartite(self,start):
#         0 no color, 1 yellow, -1 green
        queue=[]
        color=[0*6]
        visited={}
        queue.push(start)
        color[start]=1
        while(queue):
            trav=queue[0]
            queue.pop(0)
            print(trav)
            for i in range(6):
                if self.mat[trav][i] != 0 and color[i]==0:
                    queue.push(i)
                    color[i]= -1*color[trav]
                elif  self.mat[trav][i] == 1 and color[i]==color[trav]:
                    return False
        return True
                    
                    
if __name__=='__main__':
    obj=graph()
    obj.graph()
    obj.display()