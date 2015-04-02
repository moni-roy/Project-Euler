import time
def checkdigit(n):
	cnt=0
	while n>0:
		cnt+=1
		n/=10
	return cnt

def FBO():
	a=1
	b=1
	c=2
	cn=3
	while checkdigit(c)!=1000:
		a=b
		b=c
		c=a+b
		cn+=1
	return cn
	
start = time.time()
 
ans=FBO() 

elapsed = time.time() - start
 
print("%s found in %s seconds") % (ans,elapsed)


#4782 found in 2.89433097839 seconds
