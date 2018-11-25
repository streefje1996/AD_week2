import random
import sys

sys.setrecursionlimit(1000000)

#random.randint()

def qsort(a):
    global steps
    assert len(a) > -1
    steps+=1
    if len(a) == 1:
        return [a[0]]
    if len(a) == 0:
        return []
    pivot = min(a)
    a.remove(pivot)
    left = []
    right = []
    for element in a:
        if element >= pivot:
            right.append(element)
        else:
           left.append(element)

    left = qsort(left)
    right = qsort(right)

    left.append(pivot)
    for element in right:
        left.append(element)

    return left

steps = 0

getallen = []
for i in range(10000):
    getallen.append(random.randint(-2000,2000))

print(qsort(getallen))

print(steps)
    

