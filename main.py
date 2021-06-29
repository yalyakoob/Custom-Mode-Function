def mode(tup):
    L1 = []
    i = 0
    while i < len(tup):
        L1.append(tup.count(tup[i]))
        i += 1
    d1 = dict(zip(tup,L1))
    d2 = {k for (k,v) in d1.items() if v == max(L1)}
    for num in d2:
        return num



