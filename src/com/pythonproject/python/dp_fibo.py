count=0
def fibo(n):
    global count
    count=count+1
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

def fibo_memorization(n,term):
    global count
    count=count+1
    if term[n]!=0:
        return term[n]
    term[n]=fibo_memorization(n-1,term)+fibo_memorization(n-2,term)
    return term[n]

def fibo_dp(n):
    global count
    term=[0]*1000
    count=count+1
    term[1]=1
    term[2]=1
    for i in range(3,n+1):
        term[i]=term[i-2]+term[i-1]
    return term[n]

if __name__=='__main__':
    n=10
#     global count
    count=0
    print("Recursice Fibonacci: ",end=' ')
    print(str(fibo(n))+ ' Recursive call : ' + str(count))
    
    count=0
    term=[0]*1000
    term[1]=1
    term[2]=1
#     print(term)
    print("Recursice memorised Fibonacci: ",end=' ')
    print(str(fibo_memorization(n,term))+ ' Recursive call : ' + str(count))
    
    count=0
    print("DP Fibonacci: ",end=' ')
    print(str(fibo_dp(n))+ ' Recursive call : ' + str(count))