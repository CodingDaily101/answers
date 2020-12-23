import math
import time

memo = {}
def getBinarySum(n, dp:bool):

    pow = math.log2(n)
    powint = math.floor(pow)

    remainder = int(n-math.pow(2, powint))

    if(pow == powint):
        #n is a power of 2
        return 1
    elif dp and n in memo:
        return memo[n]
    else:
        return 1 + getBinarySum(remainder, dp)

def getBinarySums(n, dp:bool):

    i=1
    sum=0
    while i <= n:
        s = getBinarySum(i, dp)
        sum += s
        if dp:
            memo[i]=s
        i+=1
    return sum


start = time.time()
result = getBinarySums(1000000, True)

print(result)
print(time.time()-start)

start = time.time()
result = getBinarySums(1000000, False)

print(result)
print(time.time()-start)
