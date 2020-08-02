def calc():
    i = input(
        "Введите желаемое арифметическое действие над числами: +, -, *, /  или '0' для выхода из калькулятора:   ")
    if i == '0':
        print("Выход из калькулятора")
    else:
        if i == '+' or i == '-' or i == '*' or i == '/':
            try:
                namber_1 = int(input("Введите натуральное число:  "))
            except Exception:
                return print("Вы ввели некоректный символ"), calc()
            try:
                namber_2 = int(input("Введите натуральное число:  "))
            except Exception:
                return print("Вы ввели некоректный символ"), calc()

            if i == '+':
                result = namber_1 + namber_2
            elif i == '-':
                result = namber_1 - namber_2
            elif i == '*':
                result = namber_1 * namber_2
            elif i == '/':
                if namber_2 == 0:
                    return print("Ошибка!!! Деление на 0"), calc()
                else:
                    result = namber_1 / namber_2

            return print("Результат:  ", result), calc()
        else:
            return print("Вы ввели некоректный символ"), calc()


calc()