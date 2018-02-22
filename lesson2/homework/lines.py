# Написать функцию, которая принимает на вход две строки.
# Если строки одинаковые, возвращает 1.
# Если строки разные и первая длиннее, возвращает 2.
# Если строки разные и вторая строка 'learn', возвращает 3.


def function(stroka1, stroka2):
    if stroka1 == stroka2:
        return 1
    elif stroka2 == "learn":
        return 3
    elif len(stroka1) <= len(stroka2):
        return 2
    else:
        return("Пизец,в задание ничего не сказано!")


inp = input("Введи первую строку! ")
inp2 = input("Введи вторую строку! ")
print(function(inp, inp2))
