from module import*
while True:
	w=input("Функция:\nДобавить сотрудника - 1\nСамая большая зарплата - 2\nСамая маленькая зарплата - 3\nСредняя зарплата - 4\nСортировка - 5")
	if w=="1":
		lisaihmine()
	elif w=="2":
		suurpalk()
	elif w=="3":
		madalpalk()
	elif w=="4":
		keskmine()
	elif w=="5":
		sorteerimine()
	else:
		("Этой функций нет")
