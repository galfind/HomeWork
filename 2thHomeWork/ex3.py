N = int(input("Введите число: "))
doubled = 1
flag = True
while flag:
    doubled *= 2
    if doubled < N:
        print(doubled)
    else:
        flag = False
