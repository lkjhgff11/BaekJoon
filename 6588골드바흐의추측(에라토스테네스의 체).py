MAX = 1000000
check = [True]*(MAX+1)
prime=[]

for i in range(2,MAX):
    if check[i]:
        prime.append(i)
        j=2
        while i*j<=MAX:  # 배수 첨에는 2*1 2*2 2*3 ...
            check[i*j]=False  # 지우는것처럼 체크!
            j+=1 # 2*1 2*2 2*3 해주기위해서 뒤에 숫자 더하는

while True:
    n=int(input())
    if n==0:
        break
    for i in prime:
        if check[n-i]==True:
            print("%d = %d + %d" %(n,i,n-i))
            break
        
            
