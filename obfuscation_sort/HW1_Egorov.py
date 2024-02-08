def hggkjhngkjg(a, b=list(0 for i in range(100))):
    chicken = 0
    egg = 0

    c = a.split()
    d = list(e for e in c if e[0] != "$")
    f = len(d)

    while chicken < f:
        g = int(d[chicken+1])
        if d[chicken][0] == 'y':           
                    b[b[g]] = egg
        if d[chicken][0] == 'p':
            if d[chicken][-2] != 'o': 
                    if egg > 0:
                        chicken = g*2
                        continue
            else:
                    chicken = g*2
                    continue
        else:
            if d[chicken][1] == d[chicken][2]:
                if d[chicken][2] == d[chicken][-1]:
                    egg = b[b[g]]
                else:
                    if egg == 0:
                        chicken = g*2
                        continue
            else:
                if d[chicken][-2] == 'n':
                    egg = egg * b[g]
        if d[chicken][3] == 't':              
                    egg = b[g]
        if d[chicken][2] != 'a':
            if d[chicken][-4] == 'g':      
                    egg = egg-b[g]
            if d[chicken][1] == "r":
                if d[chicken][0] != "d":
                    egg = egg+b[g]
                else:
                    b[g] = egg           
        else:
            if d[chicken][-2] == 'r':
                 b[g] = b[g] + 1
            else:
                if d[chicken][3] != 'k':
                    if egg >= 0:
                        chicken = g
                        continue
                else:
                    egg = egg // b[g]             
        chicken += 2

length = int(input())
array = [11, 1, 2, 0, 0, 0, 0, 0, 0, 0, length]

for i in range(length):
    array.append(int(input()))

magic = "zort 10 \
         drok 9 \
         gurp 1 \
         drok 4 \
            zort 4 \
            gurp 2 \
                peep 9 \
                beep 9 \
                poop 14 \
            drok 4 \
            zort 5 \
            frog 1 \
            drok 5 \
                poop 4 \
         zort 5 \
         frog 1 \
         drok 8 \
            zort 8 \
                peep 20 \
                poop 69 \
            gurp 1 \
            drok 8 \
            drok 4 \
                zort 4 \
                bonk 2 \
                frog 1 \
                drok 7 \
                gurp 10 \
                        peep 68 \
                        beep 68 \
                    zort 7 \
                    frog 1 \
                    gurp 10 \
                        peep 49 \
                        beep 49 \
                    zort 7 \
                    frog 0 \
                    drok 6 \
                    frog 1 \
                    drok 5 \
                    oooo 5 \
                    drok 3 \
                    oooo 6 \
                    gurp 3 \
                        peep 49 \
                        beep 49 \
                    zort 7 \
                    frog 1 \
                    drok 7 \
                zort 7 \
                frog 0 \
                drok 6 \
                zort 4 \
                frog 0 \
                drok 5 \
                oooo 6 \
                drok 3 \
                oooo 5 \
                gurp 3 \
                    peep 68 \
                    beep 68 \
                oooo 5 \
                yuck 6 \
                zort 3 \
                yuck 5 \
                zort 7 \
                drok 4 \
                    poop 23 \
            poop 17 \
                zort 10 \
                drok 9 \
                    zort 9 \
                    gurp 1 \
                        peep 75 \
                        poop 133 \
                    drok 9 \
                    frog 0 \
                    drok 8 \
                    oooo 8 \
                    drok 3 \
                    oooo 0 \
                    yuck 8 \
                    zort 3 \
                    yuck 0 \
                        zort 4 \
                        gurp 4 \
                        drok 4 \
                zort 4 \
                bonk 2 \
                frog 1 \
                drok 7 \
                gurp 9 \
                        peep 132 \
                        beep 132 \
                    zort 7 \
                    frog 1 \
                    gurp 9 \
                        peep 113 \
                        beep 113 \
                    zort 7 \
                    frog 0 \
                    drok 6 \
                    frog 1 \
                    drok 5 \
                    oooo 5 \
                    drok 3 \
                    oooo 6 \
                    gurp 3 \
                        peep 113 \
                        beep 113 \
                    zort 7 \
                    frog 1 \
                    drok 7 \
                zort 7 \
                frog 0 \
                drok 6 \
                zort 4 \
                frog 0 \
                drok 5 \
                oooo 6 \
                drok 3 \
                oooo 5 \
                gurp 3 \
                    peep 132 \
                    beep 132 \
                oooo 5 \
                yuck 6 \
                zort 3 \
                yuck 5 \
                zort 7 \
                drok 4 \
                    poop 87 \
                poop 71 \
        "

hggkjhngkjg(magic, array)
print(array[11:])