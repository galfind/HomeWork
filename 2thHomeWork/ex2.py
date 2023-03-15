from math import sqrt
def calculate(sum, mult):
    D = sum*sum + 4*mult
    if D > 0:
        sq = sqrt(D)/2
        p = b/2
        x1 = p-sq
        x2 = p+sq
        return [x1, x2]
b = int(input('Сумма: '))
c = -int(input('Произведение: '))
print(calculate(b, c))