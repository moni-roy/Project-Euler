import time
start=time.time()

ar=[True]*20000
sm=0
for x in xrange(2,int(len(ar)**0.5)+1):
	if ar[x]:
		for y in xrange(x+x,len(ar),+x):
			ar[y]=False		
prm=[]
for i in xrange(2,len(ar)):
	if ar[i]:
		prm.append(i)

def Fact(p):
	fac=1
	for i in range(0,len(ar)):
		if prm[i]*prm[i]>p:
			break
		cnt=0
		if p%prm[i]==0:
			while p%prm[i]==0:
				cnt+=1
				p/=prm[i]
		fac*=(cnt+1)
		
	if p>1:
		fac*=2
	return fac

for i in range(10,100000):
	pp=i*(i+1)/2
	if Fact(pp)>500:
		sm=pp
		break

end=time.time()-start
print ("%s Found in %s second")%(sm,end)

#76576500 Found in 2.79624390602 second




