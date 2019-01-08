a=int(input())
b=int(input())
c = list(range(1,101))
li=[]
for i in range(a,b+1):
    for j in c:
        if i==j*j:
            li.append(i)

li.sort()
sum=0
for i in li:sum=sum+i

if not li:
  print('-1')
else:
    print(sum)
    print(li[0])
