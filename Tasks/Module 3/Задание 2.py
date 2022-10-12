s = input('Введите строку: ')
x = s.find(' ')
print(s[x+1:] + s[x] + s[:x])