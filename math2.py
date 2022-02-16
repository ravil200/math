
'''
#1
lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
if lang1 in languages:
	print('lang1 is in lang')
else:
	print('lang1 is not in lang')
#2
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
print(languages)
#3
a = 7
i = 0
while True:
    a *= a
    print(a)
    i += 1
    if i == 5:
        break

a = 7
for i in range(0,5,1):
    a*=a
    print(a)
'''
#4
'''
d = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i, item in enumerate(d):
	print(i , item)

b = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in range(0,6):
	print(i, b[i])


s = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i, item in enumerate(s):
	print(i , item)

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(0,13,2):
	print(i, names[i])

a = int(input('введите число'))
if a >= 100:
	print('это число трехзначное')
	if a % 2 == 0 and a > 0:
		print('это положительное и четное число')
		if a % 31 ==0:
			print('это число делится на 31 без остатка')
			if (a >= 100 and a % 17 ==0) or (a >= 150 and a == 13**2):
				print('что-то')
			else:
				print('не что-то')
		else:
			print('не дел на 31')
	else:
		print('не полож')
else:
	print('это число не трехзначное')

num1 = -100
num2 = num1
usl1=0
usl2=0
while num1 <= 100:
    if num1 % 13 ==0:
        num1 ** 2
        usl1 += 1
        if  num1 % 2 == 1:
            usl2 += 1
    num1 +=7
a = str([i for i in range(-100, 100)])

print('генерировать 200 чисел от -100 до 100:', a)
print('кол-во чисел подходят под первое условие ', usl1)
print('кол-во чисел подходят под второе условие', usl2)
'''
