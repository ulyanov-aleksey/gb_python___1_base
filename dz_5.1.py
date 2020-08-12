from collections import namedtuple
a = namedtuple('Company', 'name profit_1 profit_2 profit_3 profit_4')

n = int(input("число предпр: "))
profit = {}


for i in range (0,n):
    i = a(
        name = input("Организация: "),
        profit_1 = int(input("Прибыль_1: ")),
        profit_2 = int(input("Прибыль_2: ")),
        profit_3 = int(input("Прибыль_3: ")),
        profit_4 = int(input("Прибыль_4: "))
    )
    print(i)
    averege_profit = (i.profit_1 + i.profit_2 + i.profit_3 + i.profit_4)/4
    profit[i.name] = averege_profit

summa = 0
for val in profit.values():
    summa = (summa + val)
print("Среднегодовая прибыль всех компаний: ", summa/n)
for val in profit.values():
    if val < summa/n:
        print("Компания с прибылью меньше средней: ", list(profit.keys())[list(profit.values()).index(val)]) # Вытаскиваем ключ по значению val в словаре
    else:
        print("Компания с прибылью больше средней: ", list(profit.keys())[list(profit.values()).index(val)])

print(profit)