import random
def makemax(ar:list):
    max = 0
    for i in ar:
        if i>max:
            max = i
    return max
N = 7
num = int(input('Введите искомое число '))
arr = []
for i in range(N):
    arr.append(int(random.randrange(-5, 10)))
print(arr)
min_num = N
flag = True
res = 0 
for i in range(len(arr)):
    if abs(num-arr[i])<min_num:
        min_num = abs(num-arr[i])
        res = arr[i]
        flag = False
    elif flag:
        res=max(arr)
print(res)
