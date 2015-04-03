import time

start=time.time()

ans=0
for a in xrange(999,100,-1):
	for b in xrange(a,100,-1):
		tm=a*b
		if tm>ans:
			st=str(a*b)
			if st==st[::-1]:
				ans=tm
end=time.time()-start

print ("%s is found in %s")%(ans,end)

#906609 is found in 0.0737910270691
