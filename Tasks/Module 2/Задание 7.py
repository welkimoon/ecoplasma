a = int(input('Введите номер года: '))
if a%100 != 0:
    print(str(a//100 + 1))
else:
    print(a//100)