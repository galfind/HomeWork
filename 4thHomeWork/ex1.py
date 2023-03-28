def arr_fill(col:list, num):
    for i in range(num):
        col.append(input(f"Введите {i} элемент массива "))
N1 = int(input("Введите размер первого массива "))
N2 = int(input("Введите размер второго массива "))
arr1 = list()
arr2 = list()
arr_fill(arr1, N1)
print("Следующий массив")
arr_fill(arr2, N2)
print(arr1, arr2)
min_arr = min(arr1,arr2)
max_arr = max(arr1,arr2)
res=set()
for i in range(min(len(arr1),len(arr2))):
    if min_arr[i] in max_arr:
        res.add(min_arr[i])
if len(res)!=0:
    print(sorted(res))
else:
    print("Нет сопоставимых значений")
