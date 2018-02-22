
groups = [
['Вася', 'Маша'],
['Оля', 'Петя', 'Гриша'],
]


message = 'Группа 1: '



for i in groups:
    message = 'Группа: '
    for d in i:
        message = message + d + ','
    print(message)

    #     print(i[g])
    #     g += 1

# g = 0
# for i in groups:
#	print(i[0:len(groups[g])])
