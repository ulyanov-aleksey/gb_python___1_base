from collections import Counter
a = hex(int(input("Введите чило в 16 формате: "), 16))
print(list(Counter(a[2:]).elements()))
b = hex(int(input("Введите чило в 16 формате: "), 16))
print(list(Counter(b[2:]).elements()))
c = hex(int(a, 16) * int(b, 16))
print(list(Counter(c[2:]).elements()))
