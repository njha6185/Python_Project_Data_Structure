import math
from lib2to3.fixer_util import find_root

class edge:
    def __init__(self):
        self.src=0
        self.dest=0
        self.weight=0
    def edge(self,s,d,w):
        self.src=s
        self.dest=d
        self.weight=w
class graph:
    def __init__(self):
        self.mat=list(list())
        self.edges=list()
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
                temp=edge()
                temp.edge(src, dest, weght)
                self.edges.append(temp)
                            
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
            
    def findRoot(self,v,parent):
        while(parent[v]!=-1):
            v=parent[v]
        return v
    def union_sets(self,src_root, des_root,parent):
        parent[src_root]=des_root
        
    def contain_cycle(self):
        parent=[]
        edge_count=14
        for i in range(9):
            parent.append(-1)
        for i in range(edge_count):
            e=self.edges[i]
            src_root=self.findRoot(e.src,parent)
            src_dest=self.findRoot(e.dest,parent)
            if src_root==src_dest:
                return True
            self.union_sets(src_root, src_dest, parent)
        return False   
     
            
if __name__=='__main__':
    obj=graph()
    obj.graph(9)
    obj.accept()
    obj.display()
    print(obj.contain_cycle())            