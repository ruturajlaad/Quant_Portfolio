import time 
import numpy as np


def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
    
def main():
    num=np.random.randint(1,25)
    print("%dth fibonacci number is:%d"%(num,fibonacci(num)))
    
startime=time.time()
timeout=time.time() + 60*2

while time.time() <= timeout:
    try:
        main()
        time.sleep(5-((time.time()-startime)%5.0))
    except KeyboardInterrupt:
        print("/nKeyboard exception received exiting...")
        exit()
        
        