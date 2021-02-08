'''
Created on 01-Aug-2020

@author: NITISH
'''
def selectionsort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j]=temp

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp                

def insertionsort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        for j in range(i-1,-2,-1):
            if temp > arr[j]:
                break
            else:
                arr[j+1]=arr[j]
        arr[j+1]=temp    

def quicksort(l,left, right):
    i=left
    j=right
    if left >= right:
        return
    while i < j:
        while i<=right and l[i]<=l[left]:
            i=i+1
        while l[j] > l[left]:
            j=j-1
            

        if i < j:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
    temp=l[left]
    l[left]=l[j]
    l[j]=temp
    quicksort(l, left, j-1)
    quicksort(l, j+1, right)    

def mergesort(l,left, right):
    if left >= right:
        return
    mid=int((left+right)/2)
    mergesort(l, left, mid)
    mergesort(l, mid+1, right)
    i=left
    j=mid+1
    t=[]
    k=0
    while (i<=mid and j<=right):
        if l[i] < l[j]:
            t.append(l[i])
            i=i+1
            k=k+1
        else:
            t.append(l[j])
            j=j+1
            k=k+1
    while i <= mid:
        t.append(l[i])
        i=i+1
        k=k+1
    while j <= right:
        t.append(l[j])
        j=j+1
        k=k+1
    for p in range(right-left+1):
        l[left+p]=t[p]                                    
            
if __name__ == '__main__':    
    arr=[44,11,55,22,66,33]
    j=0
    
    print ("Before Sorting: ")
    print(arr)
    
#     mergesort(arr, 0, len(arr)-1)
#     print("After Merge Sort: ")
#     print(arr)
    
#     quicksort(arr, 0, len(arr)-1)
#     print("After QUICKSORt Sort: ")
#     print(arr)
    
#     for i in range(1,len(arr)):
#         temp=arr[i]
#         for j in range(i-1,-2,-1):
#             if temp < arr[j]:
#                 break
#             else:
#                 arr[j+1]=arr[j]
#         arr[j+1]=temp
#     print ("After Insertion Sorting: ")
#     print(arr)

#     bubblesort(arr)
#     print ("After Bubble Sorting: ")
#     print(arr)

#     insertionsort(arr)
#     print ("After Insertion Sorting: ")
#     print(arr)

#     for i in range(len(arr)):
#         for j in range(0,len(arr)-1-i):
#             if arr[j]>arr[j+1]:
#                 temp = arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
#     print ("After Bubble Sorting: ")
#     print(arr)

#     selectionsort(arr)
#     print("After Selection Sort: ")
#     print(arr)

#     for i in range(len(arr)):
#         for j in range(i, len(arr)):
#             if arr[i] > arr[j]:
#                 temp = arr[i]
#                 arr[i]=arr[j]
#                 arr[j]=temp
#     print ("After Selection Sorting: ")
#     print(arr)