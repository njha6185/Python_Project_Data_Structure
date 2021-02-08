def operatorRank(symbol):
    if symbol == '+':
        return 1
    elif symbol=='-':
        return 1
    elif symbol=='*':
        return 7
    elif symbol=='/':
        return 7
    elif symbol=='$':
        return 10
    else:
        return 0
def calc(a,b,symbol):
    if symbol == '+':
        return a+b
    elif symbol=='-':
        return a-b
    elif symbol=='*':
        return a*b
    elif symbol=='/':
        return a/b
    elif symbol=='$':
        return pow(a, b)
    else:
        return 0

def infixToPostfix(infix):
    postfix=""
    poststack=[]
    for i in infix:
        if i.isdigit():
            postfix+=i
        elif i == '(':
            poststack.append(i)                        
        elif i == ')':
            while(poststack[-1] != '('):
                postfix+=poststack[-1]
                poststack.pop()
            poststack.pop()            
        else:
            while (poststack and operatorRank(poststack[-1]) >= operatorRank(i)):
                postfix+=poststack[-1]
                poststack.pop()
            poststack.append(i)
    while(poststack):
        postfix+=poststack[-1]
        poststack.pop() 
    return postfix 

def infixToPrefix(infix):
    Prefix=""
    Prestack=[]
    for i in infix[::-1]:
        if i.isdigit():
            Prefix+=i
        elif i == ')':
            Prestack.append(i)                        
        elif i == '(':
            while(Prestack[-1] != ')'):
                Prefix+=Prestack[-1]
                Prestack.pop()
            Prestack.pop()            
        else:
            while (Prestack and operatorRank(Prestack[-1]) > operatorRank(i)):
                Prefix+=Prestack[-1]
                Prestack.pop()
            Prestack.append(i)
    while(Prestack):
        Prefix+=Prestack[-1]
        Prestack.pop() 
    return Prefix[::-1]

def PostFixevaluation(postfix):
    stack=[]
    for i in postfix:
        if i.isdigit():
            stack.append(int(i))
        else:
            a=stack.pop()
            b=stack.pop()
            c=calc(b,a,i)
            stack.append(c)
    return stack.pop()

def PreFixevaluation(postfix):
    stack=[]
    for i in postfix[::-1]:
        if i.isdigit():
            stack.append(int(i))
        else:
            a=stack.pop()
            b=stack.pop()
            c=calc(a,b,i)
            stack.append(c)
    return stack.pop()

def check_paranthesis(li):
    opening = '({['
    closing = ')}]'
    stack=[];
    for i in li:
        if i in opening:
            stack.append(i)
        elif i in closing:
            if stack:
                a=stack.pop()
            else:
                return False
            
            if opening.find(a)!=closing.find(i):
                return False
    if not stack:
        return True
    else:
        return False
            
      
    
if __name__ == '__main__':
    infix='5+9-4*(8-6/2)+1$(7-3)'
    print(check_paranthesis(infix))
#     print('Infix String : ' + infix) 
#     print('Postfix String : ' +infixToPostfix(infix)) 
#     print('Prefix String  : ' +infixToPrefix(infix))
#     print('Evaluate Postfix  : ' + str(PostFixevaluation(infixToPostfix(infix))))
#     print('Evaluate Prefix  : ' + str(PreFixevaluation(infixToPrefix(infix))))
    
    