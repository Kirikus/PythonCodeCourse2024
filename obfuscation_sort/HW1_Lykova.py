def x(xxxxxxx):
    if len(xxxxxxx) > 1:
        xxxxxx = len(xxxxxxx) // 2
        xxxxx= xxxxxxx[:xxxxxx]
        xxxx= xxxxxxx[xxxxxx:]
        x(xxxxx); x(xxxx)
        i = xxx = xx = 0
        while i < len(xxxxx) and xxx < len(xxxx):
            if xxxxx[i] < xxxx[xxx]: xxxxxxx[xx] = xxxxx[i]; i += 1
            else: xxxxxxx[xx] = xxxx[xxx]; xxx += 1
            xx += 1
        while i < len(xxxxx): xxxxxxx[xx] = xxxxx[i]; i += 1; xx += 1
        while xxx < len(xxxx): xxxxxxx[xx] = xxxx[xxx]; xxx += 1; xx += 1
xxxxxxx = [0,0,0,1000,-1893,89,89,-89,8,4,2,5,1,0.1111]
print("Исходный массив:"); print(xxxxxxx)
x(xxxxxxx)
print("Отсортированный массив:"); print(xxxxxxx)
