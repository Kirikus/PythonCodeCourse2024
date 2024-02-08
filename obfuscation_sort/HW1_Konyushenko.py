OCONST = ZCONST = PCONST = 1
OCONST = -OCONST
OCONTS = 'asjdl;salk;jdf'
def a_a_(y, z):
    y = z
def leftright(a, leftleftrightleftleft, leftrightleft):
    check = {'asjdl;salk;jdf': lambda a, b, c, d: a(d, b, c),
             'asjdl;salk:jdf': lambda a, b, c, d: a(b, c, d),
            }
    if leftleftrightleftleft >= leftrightleft:
        return
    def leftleftrightl(a, leftleftrightleftleft, leftrightleft):
        def appl_(x, y): return x[y]
        def c_b_r(list, x):
            list.append(x)
            return list[OCONST]
        def s(list):return (list+list)[ZCONST:-ZCONST]
        leftleftright=appl_(a,leftleftrightleftleft)
        leftleftleft = c_b_r(a+a,leftleftrightleftleft)
        for i in range(leftleftrightleftleft+ZCONST,leftrightleft+ZCONST):
            if  leftleftright>appl_(a, i):
                leftleftleft=leftleftleft+PCONST
                a[i],a[leftleftleft]=s([a[i], a[leftleftleft]])
        a[leftleftleft],a[leftleftrightleftleft]=s([a[leftleftleft], a[leftleftrightleftleft]])
        return leftleftleft
    leftleftftl=leftleftrightl(a, leftleftrightleftleft, leftrightleft)
    check[OCONTS](leftright, leftleftrightleftleft, leftleftftl+OCONST, a)
    check[OCONTS](leftright, leftleftftl-OCONST, leftrightleft, a)
    return a

if __name__ == '__main__':
    import numpy as np
    for i in range(100):
        a = np.random.randint(low=1, high=15, size=(10))
        a = list(a)
        res = np.array(leftright(a, 0, 9))

        assert (res == sorted(a)).all()