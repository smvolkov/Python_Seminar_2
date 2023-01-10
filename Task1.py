from random import randint

n = int(input('Введите число монет: '))

coins = []
heads = 0
tails = 0

for i in range(n):
    coins.append(randint(0, 1))
    if coins[i] == 0:
        tails += 1
    else:
        heads += 1
print(coins)

if tails < heads:
    print(tails)
else:
    print(heads)
