from timeit import Timer
import cProfile
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


t1 = Timer("revers", "from __main__ import revers")
print("revers ", t1.timeit(number=1000), "milliseconds")

t2 = Timer("revers_2", "from __main__ import revers_2")
print("revers_2 ", t2.timeit(number=1000), "milliseconds")

t3 = Timer("revers_3", "from __main__ import revers_3")
print("revers_3 ", t3.timeit(number=1000), "milliseconds")

def main():
    revers(12345678987654321999999908987765674546547654765476476464747647647646548745874874874874)
    revers_2(12345678987654321999999908987765674546547654765476476464747647647646548745874874874874)
    revers_3(12345678987654321999999908987765674546547654765476476464747647647646548745874874874874)


cProfile.run('main()')

# revers b revers_2 различаются подходом к циклу,
# for (постоянно будет проветять) и while (ждет наступления условия)
# поэтому For дольше всех работает
# revers_2 и revers_3 значительно не отличаются при малых числа.
# с темпом увеличения значения функции - будет уменьшаться  разгица по время у фунуции revers_3 и revers_2,
# т.к. обу функции реализуютя на константной сложности