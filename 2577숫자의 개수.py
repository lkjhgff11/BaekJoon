a = int(input())
b = int(input())
c = int(input())
# a,b,c = map(int,[input(), input(), input()])

re = str(a*b*c)

for i in range(10):

    print(re.count(str(i)))
