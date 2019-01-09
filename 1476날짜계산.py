#수 3개 지구 E(1<=E<=15) 태양 S(1<=S<=28) 달 M(1<=M<=19)
#시작은 1 1 1 일년 지날때마다 세 수 1씩증가. 예를들어 15년은 15 15 15 but 1년 더 지나서 16년이되면
#1 16 16 임 이건 16년

E,S,M=map(int,input().split())

iE=1
iS=1
iM=1
y=0
while True:
    y+=1
    if E==iE and S==iS and M==iM:
        print(y)
        break
    iE+=1
    iS+=1
    iM+=1

    if iE>15:iE=1
    if iS>28:iS=1
    if iM>19:iM=1
    
    
