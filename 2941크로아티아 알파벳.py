l = ['c=','c-','dz=','d-','lj','nj','s=','z=']
n=input()
for i in range(len(l)):
    n=n.replace(l[i],str(i))#길이 셀껀데 저기 list안에 있는 단어들은 한개로 취급
print(len(n))    

