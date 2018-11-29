import random
import sys

sys.setrecursionlimit(1000000)

#random.randint()

def qsort_worstcase(a):
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

def qsort(a):
    global steps
    assert len(a) > -1
    steps+=1
    if len(a) == 1:
        return [a[0]]
    if len(a) == 0:
        return []
    pivot = random.choice(a)
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
for i in range(1000):
    getallen.append(random.randint(-2000,2000))

#print
(qsort_worstcase(getallen))

print("qsort worst: " + str(steps))

steps = 0 

#print
(qsort(getallen))

print("qsort: " + str(steps))

