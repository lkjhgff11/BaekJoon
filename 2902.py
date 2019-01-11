# -가 담긴 인덱스 다음인덱스(성) 를 저장할 변수 m
n=list(map(str,input()))
print(n[0],end="")

for i in n:
    if '-' in i:
        m=n.index('-')
        n.remove(i)
        print(n[m],end="")
        

       
     

      
   
