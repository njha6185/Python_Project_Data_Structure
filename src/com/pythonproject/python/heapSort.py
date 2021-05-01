class maxheap:
    def __init__(self,a,len1):
        self.arr=a
        self.size=0
        self.length=len1
        
    def make_heap(self):
        self.size=self.length-1
        for i in range(int(self.size/2), 0,-1):
            ci=i*2
            temp=self.arr[i]
            while(ci<=self.size):
                if (ci+1)<=self.size and self.arr[ci+1]>self.arr[ci]:
                    ci=ci+1
                if temp > self.arr[ci]:
                    break;
                self.arr[int(ci/2)]=self.arr[ci]
                ci=ci*2
            self.arr[int(ci/2)]=temp
            
    def display(self):
        print('Heap:  ')
        print(self.arr)
        
    def delete(self):
        max=self.arr[1]
        temp=self.arr[self.size]
        self.size=self.size-1
        i=1
        ci=i*2
        while(ci<=self.size):
            if (ci+1)<=self.size and self.arr[ci+1]>self.arr[ci]:
                ci=ci+1
            if temp > self.arr[ci]:
                break
            self.arr[int(ci/2)]=self.arr[ci]
            ci=ci*2
        self.arr[int(ci/2)]=temp
        return max 

def heap_sort(a,len1):
    h=maxheap(a,len1)
    h.make_heap()
    size=len1-1
    for i in range(size, 0, -1):
        max1=h.delete()
        a[size]=max1
        size=size-1
    return a
            
if __name__=='__main__':
    arr=[0,20,12,35,15,10,80,30,17,2,1]
#     h=maxheap(arr,11)
    print('arr11: ')
    print(arr)
#     h.make_heap()
#     h.display()
#     print(h.delete())
#     h.display()
    print(heap_sort(arr, 11))
    