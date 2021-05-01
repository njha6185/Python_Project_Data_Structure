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
    
    def warshallfloyd(self):
        dist =[]
        for s in range(9):
            temp=[]
            for d in range(9):
                if s == d:
                    temp.append(0)
                else:
                    temp.append(self.mat[s][d])
            dist.append(temp)
#         9 is vertex count
        for i in range(9):
            for s in range(9):
                for d in range(9):
                    if dist[s][i]!=math.inf and dist[i][d]!=math.inf and dist[s][d]>dist[s][i]+dist[i][d]:
                        dist[s][d]=dist[s][i]+dist[i][d]
        print(dist)                    
if __name__=='__main__':
    obj=graph()
    obj.graph(9)
    obj.accept()
    obj.display()
    print(obj.warshallfloyd())            