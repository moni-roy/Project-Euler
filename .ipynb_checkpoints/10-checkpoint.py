import time
start=time.time()

ar=[True]*2000000
sm=0
for x in xrange(2,int(len(ar)**0.5)+1):
	if ar[x]:
		for y in xrange(x+x,len(ar),+x):
			ar[y]=False		
for i in xrange(2,len(ar)):
	if ar[i]:
		sm+=i

end=time.time()-start
print ("%s Found in %s second")%(sm,end)

#142913828922 Found in 0.931065797806 second

