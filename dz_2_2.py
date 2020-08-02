def check_err():   # проверка на ошибки ввода данных
    try:
        a = int(input("Введите натуральное число:  "))
    except Exception:
        return print("Вы ввели некоректный символ"), check_err()
    else:
        def check_negative():
            if a > 0:
                b = str(a)
                x = 0    #счетчик четных элементов
                y = 0     #счетчик нечетных элементов
                l = len(b) - 1

                def even_odd(b, l, x, y):
                    elem = b[l]
                    while l >= 0:
                        if int(elem) % 2 == 0:
                            x = x + 1
                            l = l - 1
                            return even_odd(b, l, x, y)
                        else:
                            y = y + 1
                            l = l - 1
                            return even_odd(b, l, x, y)
                    else:
                        print(f"Чётных элементов {x}, Нечетных элементов {y}")

                even_odd(b, l, x, y)
            else:
                return print("Вы ввели ненатуральное число, повторите попытку. "), check_err()

        check_negative()

check_err()