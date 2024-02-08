import pandas as pd
import random


def f2(A,r,l):
    x = A[r]
    y = r+1
    for i in range(r+3,l+2):
        if A[i-2]<x:
            A[i-2],A[y]=A[y],A[i-2]
            y+=1
    A[r],A[y-1]=A[y-1],A[r]
    return y-1


def f1(A,r,l):
    if r<l:
        n=random.randint(r, l - 1)
        (A[n],A[r]) =(A[r], A[n])
        m = f2(A,r, l)
        f1(A,r,m)
        f1(A, m+1, l)


if __name__ == '__main__':
    x1 = pd.Series(input().split()).apply(lambda x: int(x))
    x2 = x1[0]
    for x3 in range(x1.size):
        if x1[x3] < x1[x2]:
            x2 = x3
    x1[x1.size] = x1[x2]
    f1(x1,0,x1.size-1)
    print(x1[:-1])





