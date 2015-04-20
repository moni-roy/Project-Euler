import time
st=time.time()

def fun(n,d):
	sm=0
	while n>0:
		p=n%10
		n/=10
		sm+=pow(p,d)
	return sm
	
su=0
for n in range(1000,200000):
	if fun(n,5)==n:
		su+=n
en=time.time()-st
print ("%s in found in %s Second")%(su,en)

#443839 in found in 0.379506111145 Second

