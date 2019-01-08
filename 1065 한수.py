num = int(input())
cnt = 99

if num<100:
    print(num)
    quit()

if num == 1000:
        for i in range(100,1000):
            h,t,n = str(i)[0],str(i)[1],str(i)[2]
            if int(h) - int(t) == int(t) - int(n):
                cnt+=1
else:
    for i in range(100,num+1):
        h,t,n = str(i)[0],str(i)[1],str(i)[2]
        if int(h) - int(t) == int(t) - int(n):
            cnt+=1
print(cnt)            

