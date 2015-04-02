import time
import fractions
ans=2
start=time.time()

for i in range (3,20):
	ans=ans*i/fractions.gcd(ans,i)
	
end=time.time()-start

print("%.s found in %.10lf seconds") % (ans,end)

#232792560 found in 0.0000238419 seconds
