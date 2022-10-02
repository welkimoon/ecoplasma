a = int(input('Введите целое число: '))

summ = 0

while a > 0:
    UwU = a % 10
    summ = summ + UwU
    a = a // 10

print("Сумма:", summ)