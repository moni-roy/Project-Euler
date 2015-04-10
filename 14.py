import time
st=time.time()

chain={1:1}

def fun(n):
	if not n in chain:
		if n%2:
			chain[n]=1+fun(3*n+1)
		else:
			chain[n]=1+fun(n/2)
	return chain[n]
	
mx=0
ans=0
for i in range(1,1000000):
	an=fun(i)
	if an>mx:
		mx=an
		ans=i
		
en=time.time()-st

print ("%s in found in %s second")%(ans,en)

#837799 in found in 1.9783000946 second

