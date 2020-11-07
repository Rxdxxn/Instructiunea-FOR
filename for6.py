n=eval(input("introduceti un numar:"))
s1=0
for i in range(1,n+1):
    s1+=i
print("s1=",s1)

n=eval(input("introduceti un numar:"))
s2=0
for i in range(1,n+1):
    s2+=(i-1)*i
print("s2=",s2)

n=eval(input("introduceti un numar:"))
s3=1
pr=1
for i in range(2,n+1):
	pr*=i
	s3+=pr
print("s3=",s3)

n=eval(input("introduceti un numar:"))
s4=0
for i in range(1,n+1):
	s4+=(10*i+2)
print("s4=",s4)

n=eval(input("introduceti un numar:"))
s5=0
for i in range(1,n+1):
	s5+=n/(n+1)
print("s5=",s5)

n=eval(input("introduceti un numar:"))
s6=3
for i in range(2,n+1):
	m=str(i)
	s6+=int(str('2'+m))
print("s6=",s6)