if __name__ == '__main__':
    print("Hello")
    l=[]
    l.append(10)
    l.append(20)
    l.append(30)
    l.append(40)
    print(l)
    myitr= iter(l)
    print(next(myitr))
    print(next(myitr))
    print(l.pop(-1))
    l = ['sat', 'bat', 'cat', 'mat'] 
  
    # map() can listify the list of strings individually 
    test = list(map(list, l)) 
    print(test) 
    
    statesAndCapitals = { 
                     'Gujarat' : 'Gandhinagar', 
                     'Maharashtra' : 'Mumbai', 
                     'Rajasthan' : 'Jaipur', 
                     'Bihar' : 'Patna'
                    } 
                      
    print('List Of given states and their capitals:\n') 
      
    # Iterating over values 
    for state, capital in statesAndCapitals.items(): 
        print(state, ":", capital) 