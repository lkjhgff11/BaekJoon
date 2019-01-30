# 소수를 구하는 가장 빠른 알고리즘은 루트N까지만 나누기
import math

def Prime(num):
    if num<2:
        return False #소수가아니야
    n=int(math.sqrt(num))
    for i in range(2,n+1):
        if num%i==0:
            return False
    return True

m,n=map(int,input().split())

for i in range(m,n+1):
    if Prime(i):
        print(i)

    
