import time
start=time.time()
sms=(2*1000000+3*10000+100)/6
sm=(10000+100)/2
ssm=sm*sm
ans=ssm-sms

elapsed = time.time() - start
 
print("%s found in %.10lf seconds") % (ans,elapsed)

#25164150 found in 0.0000021458 seconds
