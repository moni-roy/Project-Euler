import time
start=time.time()
fl=0
for i in xrange(1,1000,+1):
	for j in xrange(1,1000,+1):
		if fl==1:
			break
		k=1000-i-j
		if k>0:
			if i*i+j*j==k*k:
				print i*j*k
				fl=1
end = time.time()-start
print ("Time = %s")%(end)

#31875000
#Time = 0.111121892929
