N_start = int(input('Введите первое число '))
N_end = int(input('Введите количество чисел '))
N_step = int(input('Введите ша '))
End = N_start + (N_end-1) * N_step
arr = [i for i in range(N_start, End, N_step)]
print(arr)