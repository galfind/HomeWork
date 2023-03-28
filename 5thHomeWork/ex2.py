def rec(base, exp):
    if (exp == 0):
        return (base)
    if (exp != 0):
        return rec(base+1, exp - 1)
base = int(input("Введите 1 число: "))
exp = int(input("Введите 2 число: "))
print("Результат сложения равен:", rec(base, exp))