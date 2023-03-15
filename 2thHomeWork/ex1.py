import random
coins = []
amount = int(input('Введите количество монеток: '))
for i in range(amount):
    coins.append(int(random.randrange(0, 2)))
print(coins)
counter_zero,counter_ones = 0,0
for i in coins:
    if coins[i]==0:
        counter_zero +=1
    else:
        counter_ones +=1
if counter_ones>counter_zero:
    print(f'Минимальное количество монеток, которые нужно перевернеуть {counter_zero} в сторону 0')
else:
    print(f'Минимальное количество монеток, которые нужно перевернеуть {counter_ones} в сторону 1')