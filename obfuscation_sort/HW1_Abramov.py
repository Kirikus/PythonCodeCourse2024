def f_s(a, n1):
    OOOOOO0OO0OO00OOO = max(a)
    OOOOO00OOO0OOO0OO = min(a)
    num1 = OOOOOO0OO0OO00OOO  -OOOOO00OOO0OOO0OO
    num2 = num1  /n1
    b = []
    result = []
    result2 = []
    for i in range(n1):b.append([])
    for j in range(len(a)):
        razn = (a[j]   -OOOOO00OOO0OOO0OO) / \
               num2   -int((a[j]   -OOOOO00OOO0OOO0OO)   /
                           num2)
        if razn   \
        ==0   \
                and a[j]   !=OOOOO00OOO0OOO0OO:
            b[int((a[j]     -OOOOO00OOO0OOO0OO)
                                                     /num2)  -1].append(a[j])
            result.append(1)
        else:b[int((a[j]   -OOOOO00OOO0OOO0OO)   /num2)].append(a    [j])
        result2.append(num1)

    for i in range(len(result)):
        if result2[i] \
                - result[i]>0: result2[i]=   \
            OOOOOO0OO0OO00OOO

    for i in range(len(b)):
        if len(b[i])   \
        !=0:b[i].sort()
    f = 0
    for i in b:
        if i:
            for j in i:
                a[f]=j
                f=f+1
a = [1, 1.2, 3, 7, 4.5, 19, 12, 3.8, 11.1, 1.5]
N = 5
f_s(a, N)
print(a)
