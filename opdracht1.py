
def machtv3(a,n):
    assert n > 0
    count = 0
    m = 1
    while n > 0:
        count+=1
        if n%2 == 0:
            n = n / 2
            a = a * a
        else:
            n = n -1
            m = m * a
    return m, count

print(machtv3(2,5))