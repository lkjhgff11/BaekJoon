c=int(input())
for i in range(c):
    score=list(map(int,input().split()))
    n=score[0]
    score=score[1:]
    avg = sum(score)/n
    cnt = 0
    for j in score:
        if j > avg:
            cnt+=1
    student=(100*cnt)/n
    print("%.3f%%" %student)

