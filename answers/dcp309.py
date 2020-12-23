
import math
#define input

input = [0,1,1,0,1,0,0,0,1, 1, 1, 0]

def countSide(ar:list):
    head=0
    tail= len(ar)-1
    count =0

    while head < tail:

        while head< len(ar) and ar[head] != 0:
            head+=1

        while tail>0 and ar[tail] != 1:
            tail-=1

        if head<tail and ar[head]==0 and ar[tail]==1:
            count+= tail-head
            head+=1
            tail-=1

    return count


def countMin(ar: list):
    # find the pivot

    m = sum(ar)

    j=0
    for i,v in enumerate(ar):
        if j== math.ceil(m/2):
            pivot = i
        if v ==1:
            j+=1

    #count the moves on both sides
    left = countSide(list(reversed(ar[:pivot])))
    right = countSide(ar[pivot:])

    return left+right


result = countMin(input)
print(result)