
#define the input

memo={}

import math
import time

def getNumBit(n, dp:bool):
# get sum of set bits
    pow = math.log(n, 2)
    powint = math.floor(pow)

    remainder = n - math.pow(2, powint)

    if pow == powint:
        return 1
    elif dp and n in memo:
        return memo[n]
    else:
        return 1 + getNumBit(remainder, dp)



def getNumBits(n, dp:bool):

    i=1
    total =0
    while i<=n:
        # loop through values 1 to N
        sum = getNumBit(i, dp)
        memo[i] = sum
        total += sum
        i+=1

    # return total
    return total

N=1000000
start = time.time()
result = getNumBits(N, False)
print(time.time()-start)
print(result)

start = time.time()
result = getNumBits(N, True)
print(time.time()-start)
print(result)
