num = input("Введите номер билета: ")
num1 = num[:3]
print(num1)
num2 = num[3:]
print(num2)
res1,res2 = 0,0
for res in num1:
    res1 += int(res)
for res in num2:
    res2 += int(res)
num1 = " + ".join(num1)
num2 = " + ".join(num2)
print(res1, res2)
if res1==res2:
    print("Билет счастливый")
    print(num1, " = ", num2)
else:
    print('Не повезло')