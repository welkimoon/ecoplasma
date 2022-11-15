numbers = [int(x) for x in input("Последовательность: ").split()]

seen = set()

for number in numbers:
    if number in seen:
        print("дап")
    else:
        print("ноуп")
        seen.add(number)