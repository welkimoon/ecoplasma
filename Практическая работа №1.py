import random

ver = 0
ver2 = 0

for i in range(100000):
    a = [0, 0, 1]
    b = random.choice(a)
    a.remove(b)
    if b == 1:
        ver += 1
    else:
        a.remove(0)
    if a[0] == 1:
        ver2 += 1
print(ver//1000, ver2//1000)
