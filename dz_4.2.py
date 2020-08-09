from timeit import Timer


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return (f'{str(number % 10)}{recursive_reverse(number // 10)}')

t1 = Timer("recursive_reverse(12345678987654321)", "from __main__ import recursive_reverse")
print("recur ", t1.timeit(number=1000)/1000, "milliseconds")
## рукурси и постоянный пересчет элементов заметно увеличивают время работы коды

def memorize(func):
    def g(n, memory = {}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g

@memorize
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return (f'{str(number % 10)}{recursive_reverse(number // 10)}')



t2 = Timer("recursive_reverse(12345678987654321)", "from __main__ import recursive_reverse")
print("memory ", t2.timeit(number=1000)/1000, "milliseconds")

## мемоизация в разы уменьшает время работы кода, т.к. происходит подсчет только новых элементов,
# а уже посчитаные сохраняются в словаре memory
# timeit(number=1000)/1000 - это среднее время 1000 вызовов