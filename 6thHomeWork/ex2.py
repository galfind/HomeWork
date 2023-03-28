input_arr = '-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7'
arr = input_arr.split(', ')
lower = int(input('Введите нижний предел '))
upper = int(input('Введите верхний предел '))
print([i for i in arr if int(i)>lower and int(i)<upper])