n = int(input('Введите число N: '))

for i in range(2, n+1):
    if n % i == 0:
        print(i)
        break