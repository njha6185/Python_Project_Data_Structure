'''
Created on 26-Jul-2020

@author: NITISH
'''
from builtins import int
def Linear_Search(fac,a):
    for i in range(len(fac)-1):
        print (str(a) + "==" + str(fac[i]))
        if a==fac[i]:
            return i
        
    return -1
        
if __name__== '__main__':
    fac=[121,234,23,41,15,6];
    a=int(input("Enter No. : "))
#     for i in range(a+1):
#         if i != 0 :
#             fac=fac*i
#     print(fac)
#==============================
    k=Linear_Search(fac,a)
    if k != -1:
        print("Found at position : " + str(k))
    else:
        print("Not found")
            