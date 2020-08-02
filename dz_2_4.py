def check_err():  # проверка на ошибки ввода данных
    try:
        n = int(input("Введите количество элементов:  "))
    except Exception:
        return print("Вы ввели некоректный символ"), check_err()
    else:
        def check_negative():
            if n > 0:
                a = []
                k = n
                a.append(1)
                def namber_list(a, k):
                    while k != 1:
                        if k % 2 == 0:
                            a.append(float(a[-1]) * -0.5)
                            k = k - 1
                            return namber_list(a, k)
                        else:
                            a.append(float(a[-1]) * -0.5)
                            k = k - 1
                            return namber_list(a, k)
                namber_list(a, k)
                print(f"Список из {n} элементов:  {a}")

                def sum_arg(arg, size):
                    if (size == 0):
                        return 0
                    else:
                        return arg[size - 1] + sum_arg(arg, size - 1)

                a = sum_arg(a, n)
                print("Сумма всех элементов списка:  ", a)
            else:
                return print("Вы ввели ненатуральное число, повторите попытку. "), check_err()

        check_negative()

check_err()