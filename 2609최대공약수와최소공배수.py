# 재귀를 사용해서 구현한 유클리드 호제법
def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)


n,m= map(int,input().split())

print(GCD(n,m))
print(n*m//GCD(n,m))
