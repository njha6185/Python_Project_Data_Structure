import math
class graph:
    def __init__(self):
        self.mat=list(list())
    def graph(self,size):
        for i in range(size):
            temp=[]
            for j in range(size):
                temp.append(math.inf)
            self.mat.append(temp)
    def accept(self):
#         print(self.mat)
        edge_cnt=int(input('Enter No of Edges'))
        if edge_cnt != 0:
            for i in range(edge_cnt):
                src=int(input('Enter src '))
                dest=int(input('Enter dst'))
                weght=int(input('Enter weight'))
                self.mat[src][dest]=weght
                self.mat[dest][src]=weght            
        else:
            self.mat=[[math.inf, 4, math.inf, math.inf, math.inf, math.inf, math.inf, 8, math.inf],        
                        [4, math.inf, 8, math.inf, math.inf, math.inf, math.inf, 11, math.inf],
                        [math.inf, 8, math.inf, 7, math.inf, 4, math.inf, math.inf, 1],
                        [math.inf, math.inf, 7, math.inf, 9, 14, math.inf, math.inf, math.inf],
                        [math.inf, math.inf, math.inf, 9, math.inf, 10, math.inf, math.inf, math.inf],
                        [math.inf, math.inf, 4, 14, 10, math.inf, 2, math.inf, math.inf],
                        [math.inf, math.inf, math.inf, math.inf, math.inf, 2, math.inf, 1, 6],
                        [8, 11, math.inf, math.inf, math.inf, math.inf, 1, math.inf, 7],
                        [math.inf, math.inf, 1, math.inf, math.inf, math.inf, 6, 7, math.inf]]
        
    def display(self):
        for i in self.mat:
            print(i)
    def getMin(self,key,mst):
        min_key=math.inf
        min_vert=0
        for i in range(9):
            if(mst[i]==False and key[i]<min_key):
                min_key=key[i]
                min_vert=i
        return min_vert
    
    def prim(self,start):
        mst=[]
        key=[]
        parent=[]
        for i in range(9):
            mst.append(False)
            key.append(math.inf)
            parent.append(-1)
#         print(mst)
        
        key[start]=0        
        
        for i in range(9):
            cur=self.getMin(key, mst)
            mst[cur]=True
            for j in range(9):
                if self.mat[cur][j] != math.inf and mst[j]==False and key[j]>self.mat[cur][j]:
                    key[j]=self.mat[cur][j]
                    parent[j]=cur
        for i in range(9):
            print(str(i)+'->'+str(parent[i]))
        
     
            
if __name__=='__main__':
    obj=graph()
    obj.graph(9)
    obj.accept()
    obj.display()
    obj.prim(0)            