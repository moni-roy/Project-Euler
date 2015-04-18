import time
st=time.time()

fac=[1]
for i in range(1,41):
	fac.append(fac[i-1]*i)
	
an=fac[40]/fac[20]/fac[20]

en = time.time()-st;

print ("%s found in %.10lf seconds")%(an,en)

#137846528820 found in 0.0000269413 seconds
