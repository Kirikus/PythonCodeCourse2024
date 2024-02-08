def sort(lst):
    class letter:
        def __init__(self, x = "0"):
            try:
                int(x)
            except ValueError:
                print("author of the code is a dummass")
            self.val = x
        def __str__(self):
            return self.val
        def get(a):
            if (a == ""):
                return 0
            else:
                return (get(a[:-1]) << 1) + int(a[-1])
    
        def __gt__(self, other):
            return get(self.val) < get(other.val)
        def Decrease(self):
            if (self.val == "-1"):
                return "0"
            elif (self.val == "1"):
                return "10"
            elif (self.val[-1] == "0" and (len(self.val) > 1) and self.val[-2] == "0"):
                return self.val[:-2] + "01"
            elif (self.val[-1] == "0" and (len(self.val) > 1) and self.val[-2] == "1"):
                return self.val[:-2] + "11"
            elif (self.val == "0"):
                return "1"
            else:
                return letter(self.val[:-1]).Decrease() + "0"
        def Increase(self):
            if (self.val == "0"):
                return "-1"
            elif (self.val[-1] == "1"):
                return self.val[:-1] + "0"
            else:
                return letter(self.val[:-1]).Increase() + "1"
    Idx = letter("0")
    idX = letter("0")
    def get(a):
        if (a == ""):
            return 0
        else:
            return (get(a[:-1]) << 1) + int(a[-1])
      
    for i in lst:
        idX.val = idX.Decrease()
    
    idX.val = idX.Increase()
    
    u = 0
    
    while Idx > idX:
        for i in range(get(Idx.val), get(idX.val), 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        idX.val = idX.Increase()

        for i in range(get(idX.val), get(Idx.val), -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        Idx.val = Idx.Decrease()
        u += 1
    return lst
