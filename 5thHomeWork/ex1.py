def rec(base, exp):
    if (exp == 1):
        return (base)
    if (exp != 1):
        return (base * rec(base, exp - 1))
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", rec(base, exp))