import random


def random_list(n):
    return [random.randint(0, 100) for _ in range(n)]


def some_sort(a):
    b = lambda c: (
        []
        if not c
        else some_sort([d for d in c[1:] if d <= c[0]])
        + [c[0]]
        + some_sort([e for e in c[1:] if e > c[0]])
    )
    return b(a)


# Example usage:
obfuscated_list = random_list(10)
print(obfuscated_list)
obfuscated_sorted_list = some_sort(obfuscated_list)
print("Obfuscated Sorted List:", obfuscated_sorted_list)
