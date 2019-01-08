for i in range(3):
    a,b,c,d = map(int,input().split())
    
    head=0
    back=0
    if a == 0 : head = head+1
    if b == 0 : head = head+1
    if c == 0 : head = head+1
    if d == 0 : head = head+1

    if a == 1 : back = back+1
    if b == 1 : back = back+1
    if c == 1 : back = back+1
    if d == 1 : back = back+1

    if head==1: print("A")
    elif head==2: print("B")
    elif head==3: print("C")
    elif head==4: print("D")
    elif back==4: print("E")    
    

