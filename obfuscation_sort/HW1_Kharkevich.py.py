def oddevensort(a, n, i):
# ______________$$_____________________ $$
    j = i 
# ____________$$$__$__________________$__$$$
    а = 2*n//(2+n)*0+n
# ___________$$$___$$________________$$___$$$
    o = 2 * i + 1 
# ___________$$$$$$$$________________$$$$$$$$
    о = 2 * i + 2 
# ____________$$$$$$__________________$$$$$$
    if o < а and a[i] < a[o]:
# _____________$$$$____$$0$$$$$0$$$____$$$$ 
        j = o
# _______________$$__$$$$$$$$$$$$$$$$__$$
    if о < а and a[j] < a[о]:
# ___________$$___$$$$$$$$$$$$$$$$$$$$$$___$$
        j = о
# _________$$__$$__$$$$$$$$$$$$$$$$$$$$__$$__$$
    if j != i:
# ________$______$$$$$$$$$$$$$$$$$$$$$$$$______$
        (a[i], a[j]) = (a[j], a[i])
# ________$__$$$____$$$$$$$$$$$$$$$$$$____$$$__$
        oddevensort(a, n, j)
# __________$___$$$$_$$$$$$$$$$$$$$$$_$$$$___$
def trytoguess(а):
# _________$_________$_$$$$$$$$$$$$_$_________$
    с = len(а)
# _________$______$$$________________$$$______$
    c=0
# _______________$______________________$
    for i in range(с // 2, -1, -1):
# ______________$________________________$
        oddevensort(а, с, i)
# ______________$_______________________ _$
    for i in range(с - 1, c, -1):
# ______________$_______________________ _$
        (а[i], а[c]) = (а[c], а[i])
# ______________$_______________________ _$
        oddevensort(а, i, c)
