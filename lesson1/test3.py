s_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']
g = 0
for i in names:
	print(s_male[i])
	if s_male[i]:
		print(names[g] +" " +  "m")
	else:
		print(names[g] +" " +  "w")
