def map1(fn, a):
    i = 0
    b = []
    while i != len(a):
        print(len(a))
        i += 1
        b.append(fn(a[i]))
    return b

