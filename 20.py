import time
st=time.time()

fact=1
for i in range(2,101):
	fact*=i
fa=str(fact)
sm=0
for i in range(0,len(fa)):
	sm+=int(fa[i])

en=time.time()-st

print ("%s in found in %s")%(sm,en)

#648 in found in 0.00018310546875

