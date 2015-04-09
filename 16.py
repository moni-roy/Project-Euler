import time
start=time.time()

sr=''
sr=str(2**1000)
sm=0
for i in xrange(0,len(sr),+1):
	sm+=int(sr[i])

end=time.time()-start

print ("%s in found in %s second")%(sm,end)

#1366 in found in 0.000247955322266 second
