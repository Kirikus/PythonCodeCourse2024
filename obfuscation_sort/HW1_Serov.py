a = [3, 1, 2, 0, -1, 15, 99, 100]

f = lambda z: z if len(z) <= 1 else (lambda f: f(f))(lambda g: lambda l: l if len(l) <= 1 else g(g)([x for x in l[1:] if x <= l[0]]) + [l[0]] + g(g)([x for x in l[1:] if x > l[0]]))([x for x in z[1:] if x <= z[0]]) + [z[0]] + (lambda f: f(f))(lambda g: lambda l: l if len(l) <= 1 else g(g)([x for x in l[1:] if x <= l[0]]) + [l[0]] + g(g)([x for x in l[1:] if x > l[0]]))([x for x in z[1:] if x > z[0]])
 
print(f(a))