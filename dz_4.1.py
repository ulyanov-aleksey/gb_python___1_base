from timeit import Timer

def func_1():
    new_arr = []
    for i in range(10000):
        if i % 2 == 0:
            new_arr.append(i)
    return (new_arr)
#  сложность линейная, будет увеличиваться время в зависимости от количества элементов

def func_2():
    my_lst = list(range(0, 10000, 2))
    return (my_lst)
# сложность константная, время не зависит от количества элементов

t1 = Timer("func_1()", "from __main__ import func_1")
print("append ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("func_2()", "from __main__ import func_2")
print("list ", t2.timeit(number=1000), "milliseconds")