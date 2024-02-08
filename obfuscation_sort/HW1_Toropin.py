from functools import wraps as w
import functools as f

def s(l):
    @w(w(lambda x: x))
    def u(d):
        @w(w(lambda x: x))
        def v(g):
            def t(*args, **kwargs):
                result = d(*args, **kwargs)
                return g(result[::-1])
            return t
        
        @v
        def e(d):
            c = len(d)
            _ = (lambda f: f(f))(lambda f: lambda d, i=0: d if i == c else f(f)(d, i + 1) if (lambda x: x[0] > x[1])(d[i - 1:i + 1]) else (lambda x: x)(d.__setitem__(i, d[i - 1]), d.__setitem__(i - 1, d[i])))
        
        return e
    
    return u

@w(w(w(w(w(w(f.partial)))))))
def a(d):
    return d

# sorted_array = a(s(s(original_array)))
