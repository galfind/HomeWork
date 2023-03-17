import random
N = int(input('Введите размер массива '))
arr = []
for i in range(N):
    arr.append(int(random.randrange(0, 10)))
print(arr)
print(arr.count(5))