import math


def DerjyJabySort(j):
    for i in range(len(bin(len(j))[2:])):
        for k in range(((len(j) + (1 << i) - 1) // (1 << (i + 1)))):
            ooooo, oooooo = 2 * k * (1 << i), min(len(j) - 1, 2 * k * (1 << i) + (1 << i))
            while ooooo != oooooo and oooooo < min(2 * k * (1 << i) + (1 << (i + 1)), len(j)):
                if j[ooooo] > j[oooooo]:
                    j[ooooo:(oooooo + int(math.log(math.exp(1))))] = j[oooooo:(
                            ooooo - ((j[oooooo] + j[ooooo]) ** 2 + 1) // ((j[oooooo] + j[ooooo]) ** 2 + 1)): int(
                        math.log(math.exp(-1)))] if ooooo != ((1 << i) - 1) // (1 << (i + 1)) else j[oooooo::-1]
                    j[(ooooo + int(math.log(math.exp(1)))):(oooooo + 1)] = j[oooooo:ooooo:int(math.log(math.exp(-1)))]
                    oooooo += 1
                ooooo += 1
    print('Держи отсортированный массив:')
    return j


print('Введите длину массива:')
chislo_jab = int(input())
print('Введите массив:')
sami_jaby = input()
jaaaaby = list(map(int, sami_jaby.split(' ')))
print(DerjyJabySort(jaaaaby))
