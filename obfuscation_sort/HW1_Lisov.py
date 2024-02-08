def booba(a):return a if len(a) <= 1 else booba([x for x in a[1:] if x <= a[0]]) + [a[0]] + booba([x for x in a[1:] if x > a[0]])
