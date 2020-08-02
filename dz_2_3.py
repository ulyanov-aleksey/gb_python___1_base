#########  ПЕРВЫЙ ВАРИАНТ ПЕРЕВОД ЧИСЛА В СПИСОК

def check_err():  # проверка на ошибки ввода данных
    try:
        a = int(input("Введите натуральное число:  "))
    except Exception:
        return print("Вы ввели некоректный символ"), check_err()
    else:
        def check_negative():
            if a > 0:
                b = str(a)
                c = list(b)
                c_rev = []

                def reverse(c):
                    if len(c) == 1:
                        c_rev.append(c[0])
                        return
                    c_rev.append(c[-1])
                    return reverse(c[0:len(c) - 1])

                reverse(c)
                print(c_rev)
            else:
                return print("Вы ввели ненатуральное число, повторите попытку. "), check_err()

        check_negative()


check_err()

### ВТОРОЙ ВАРИАНТ ВАШ (с числовыми данными) не использовал, т.к Вы его скинули для ознакомления с рекурсией

def recur_method(numb, flip=0):
    """Рекурсия"""
    if numb == 0:
        return flip
    else:
        flip = (flip * 10) + (numb % 10)
        numb = numb // 10
        return recur_method(numb, flip)


try:
    NUMB = int(input("Введите число: "))
    print(f"Перевернутое число: {recur_method(NUMB)}")
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")