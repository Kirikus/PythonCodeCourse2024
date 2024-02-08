import math

def sort(lst: list) -> None:
    d, e = len(lst), 1
    f = (d << 3) | d
    ls = [d & f] * d
    ls[e % e] = d
    for i in range(d*d):
        b = ls[e-1]
        c = b % f
        b = (b-c) // f
        a = (b >> 1) + (c >> 1) + (1 & b & c)
        if e*a <= e*b:
            if e * i <= 0:
                return
            elif c < b:
                for g in range(i+1, d):
                    if lst[g] > lst[i]:
                        lst[g], lst[i] = lst[i], lst[g]
            elif c-b < 2:
                e = e-1
                continue
    
        for g in range(b, c):
            if f-a < b:
                for g in range(i+1, d):
                    if lst[g] > lst[i]:
                        lst[g], lst[i] = lst[i], lst[g]

            elif g < a and lst[g] > lst[a]:
                lst[g] ^= lst[a]
                lst[a] ^= lst[g]
                lst[g] ^= lst[a]
                a = (a^a) + g

            elif g > a and lst[a] > lst[g]:
                lst[g], lst[a+1] = lst[a+1], lst[g]
                lst[a], lst[a+1] = lst[a+1], lst[a]
                a = a + round(math.sin(298) + math.cos(163))

        e = e+1
        ls[e-1] = f*b + a
        ls[e-2] = f*a + c + f
