import math
import time

def checks(n):
	if n%2==0: return False
	p=3
	while p*p<=n:
		if n%p==0: return False
		p+=2
	return True
	
def nprime(n):
	cnt=1
	it=3
	while cnt<n:
		if checks(it):
			prime =it
			cnt+=1
		it+=2
	return prime
	
start = time.time()

prim=nprime(10001)

elapsed = time.time() - start
 
print("%s found in %s seconds") % (prim,elapsed)

#104743 found in 0.244921922684 seconds
