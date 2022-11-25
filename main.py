# print('GB Lesson 1')
#  все переменные через _ и с маленькой буквы
# //целое число от деления
num1 = '15' #строки с  " " или ' '
num2 = '7'
num1, num2 = num2, num1 #поменять местами
print(f'Любой вывод {num1}, {num2}')
print('Любой вывод' , num1 , num2)
#num3 = num1 * 7 строку умножить на число = повторение
a = input() #по умолчанию тип string в переменой а
print('Любой вывод' , num1 , num2, sep='****', end='---')
# b = int(a) переводим переменную а в int  и записываем в
c = int(input('Введите число : ')) #int/string/bool/float перед() означает тип
num1 = 1
num2 = 1
if num1 > num2:
    print(1)
elif num2 > num1:
    print(2)
else:
    print(3)