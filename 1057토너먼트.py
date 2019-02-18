n,jimin,hansu=map(int,input().split())

mans = list(range(1,n+1))
cnt=0

# while 우승자가 나올때 까지
    # 매 라운드가 실행되지
        # 매 라운드에서는 살아남아있는 사람들끼리 2명씩 짝을 지어서 대전을 한다.

#리스트의 원소가있는동안(True로 침)
while mans:
    cnt+=1
    winners = []
    for i in range(len(mans)//2):
        a=mans.pop(0)
        b=mans.pop(0)

        # if (jimin, hansu) in ((a,b), (b,a))
        if (a==jimin and b==hansu) or (a==hansu and b==jimin):
            print(cnt)
            mans=[]
            break
        if a in (jimin,hansu):
            winners.append(a)
        elif b in (jimin,hansu):
            winners.append(b)           
        else:
            winners.append(a)     
    mans = winners + mans
