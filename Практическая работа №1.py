import random

win_with_change = 0
win_without_change = 0

for i in range(100000):
    a = [0, 0, 1]
    b = random.choice(a)
    a.remove(b)
    if b == 1:
        win_with_change += 1
    else:
        a.remove(0)
    if a[0] == 1:
        win_without_change += 1

print(
    f"""Шанс победы не меняя выбор: {win_with_change//1000}%
Выбор менялся: {win_without_change//1000}%"""
)