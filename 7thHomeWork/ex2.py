def print_operation_table(operation, num_rows, num_сolumns):
    arr = [[operation(i,j) for i in range(1, num_rows+1)] for j in range(1,num_сolumns+1)]
    print (arr)
    for i in arr:
        print(*[f"{x:>3}" for x in i])
    
line = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))
print_operation_table(lambda x,y: x*y,line,columns)