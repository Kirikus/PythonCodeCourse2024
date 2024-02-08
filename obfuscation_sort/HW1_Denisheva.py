import sys

class _Getch:
    def __init__(self, inputs):
        self.inputs = inputs;self.index = 0
    def __call__(self):
        if self.index < len(self.inputs):
            val = self.inputs[self.index];self.index += 1
            return val
        else:
            return 0
def ooooo(aaaaaaaaaa):
  aaaaaaaaaa= cleanup(list(aaaaaaaaaa));aaaa = bbb(aaaaaaaaaa);aaa, aa, aaaaa = [0], 0, 0
  while aa < len(aaaaaaaaaa):
    aaaaaa = aaaaaaaaaa[aa]
    if aaaaaa == ">":
      aaaaa += 1
      if aaaaa == len(aaa): aaa.append(0)
    if aaaaaa == "<": aaaaa = 0 if aaaaa <= 0 else aaaaa - 1
    if aaaaaa == "+":
      aaa[aaaaa] = aaa[aaaaa] + 1 if aaa[aaaaa] < 255 else 0
    if aaaaaa == "-":
      aaa[aaaaa] = aaa[aaaaa] - 1 if aaa[aaaaa] > 0 else 255
    if aaaaaa == "[" and aaa[aaaaa] == 0: aa = aaaa[aa]
    if aaaaaa == "]" and aaa[aaaaa] != 0: aa = aaaa[aa]
    if aaaaaa == ".": sys.stdout.write(str(ord(chr(aaa[aaaaa]))));sys.stdout.write(' ')
    if aaaaaa == ",": aaa[aaaaa] = ord(chr(getch()))
    aa += 1
def cleanup(aaaaaaaaaa):
  return ''.join(filter(lambda aaaaaaaaaaa: aaaaaaaaaaa in ['.', ',', '[', ']', '<', '>', '+', '-'], aaaaaaaaaa))
def bbb(aaaaaaaaaa):
  aaaaaaa, aaaa = [], {}
  for aaaaaaaaa, aaaaaa in enumerate(aaaaaaaaaa):
    if aaaaaa == "[": aaaaaaa.append(aaaaaaaaa)
    if aaaaaa == "]":
      start = aaaaaaa.pop();aaaa[start] = aaaaaaaaa;aaaa[aaaaaaaaa] = start
  return aaaa
def main():
    aaaaaaaaaaaaa = """
>,[>+[->+<],]>[->>>>>>>>>>>>>>>+<<<<<<<<<<<<<<<]>>>>>>>>>>>>>>+[[-<
+<+>>]<[->+<]<-[-<<[<]<<<<<<<<<<<<[->>>>>>>>>>>>+<<<<<<<<<<<<]>>>>>
>>>>>>>[>]>]>>>[-<<+<+>>>]<<[->>+<<]<[-<<[<]<<<<<<<<<+>>>>>>>>>>[>]
>]<<[<]<<<<<<<<<[-<<[<]<[->+<]>[>]>]<<[->>>>+<<<<]<[[->+>+<<]>>[-<<
+>>]<[->>[>]>>>>+<<<<<[<]<]>>[>]>>[->+<<<+>>]>[-<+>]>[-<+>]<<>>+<<[
->[->]>[<<[-]>>->>]<<+<<]>[[-]<+>]<[->+<]<<[->>+<<]>>>[->-<<<<<[<]<
<[->>>[>]>>>>>>>>+<<<<<<<<<[<]<<]>>>[>]>>>>>>>+[-<+>]<<<<<<<<[<]>[[
-<+>]>]>[-<+>]>[-<+>]]>[-<<<+<<[<]<<[->>+<<]>>[>]>>>>]<<<<<[<]<<]>>
>[>]>>>>>>>[[-<+<+>>]<[->+<]>[->>[>]>[>]>>+<<<[<]<<[<]<]>>[>]>[>]>>
>[-<<<+>>>]<<<[->>>+[>]>+<<[<]<]>>[-<+>]<[->>[>]>>+<<<[<]<]>>[>]>[[
-<+>]>]<<[<]<<<[<]<[<]<]<<<<<<[[->>>>>>>>[>]>[>]>>>[>]>>+<<<[<]<<<[
<]<[<]<<<<<<<]>>>>[->>>>[>]>[>]>+<<[<]<[<]<<<]>>>>[>]>[>]>>>[-<+<+>
>]<[->+<]<+[->>[>]>+<<[<]<]>>[>]>[[-<+>]>]<<[<]<<<[<]<[<]<<<<<<<]<<
[<]>[[-<<<+>>>]>]>>[-<<<<<+>>>>>]>>>[-]>>>>[[-<<<<<<<<<<<+>>>>>>>>>
>>]>]>[[-<<<<<<<<<<<<+>>>>>>>>>>>>]>]>>>[-]>[-]>[[-<<+>>]>]<<<[<]>]
<<<<<<<<<<<<<<<<[<]>[.>]
    """
    # input data from 1 to 255
    input = [19, 7, 8, 3, 255, 1, 133]
    ooooooo = ''.join(chr(num) for num in input)
    oooooooo = [ord(c) for c in ooooooo]
    global getch
    getch = _Getch(oooooooo)
    ooooo(aaaaaaaaaaaaa)
if __name__ == "__main__": main()
