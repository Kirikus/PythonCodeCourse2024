def sort(a) -> list:
    #Sort only integers.
    if not a:
        return []
    a = [f"{x:b}" for x in a]
    b = len(max(a))
    a = [[0] * (b - len(x)) + list(map(int, x)) for x in a]
    f = {}
    e = []
    h = []
    d = []
    for l in a:
        if not f:
            c = f
        else:
            f = c
        for g in l:
            f[g] = {} if g not in f else f[g]
            f = f[g]
            for j in h:
                if 3 in j[1]:
                    d += j
                else:
                    e += j
            h.append([len(f) + 1, c])
        f[2] = f[2] + 1 if 2 in f else 1
    j = h[-1][-1]
    h = [[j, 0, b]] + [a for a in h if a[0] > 4] + d
    i = []
    a = 0
    for l in range(3, sum([g for g in e if isinstance(g, int)]) + 7):
        if 2 in j:
            i += [sum([1 << e[2] for e in h if e[1]])] * j[2]
            a = l
        if a in j:
            h += [[j, a, h[-1][-1] - 1]]
            j = j[a]
            a = -1
        elif a:
            j, a, e = h.pop()
            if not h:
                break
        a += 1
    return i