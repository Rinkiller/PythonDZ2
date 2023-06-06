# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

def NOK(num1,num2):
    if num2 == 0:
        return num1
    return NOK(num2, num1 % num2)

def summOrProizvDrob(str1 , str2 , operation):
    if str1 == None or str2 == None:
        return None
    listOfstrings = (str1 + '/' + str2).replace(" ","").split('/')
    for el in listOfstrings:
        if not el.isdigit():
            raise Exception('Одно из переданных значений не является числом')
    if operation == '+':
        Delimoe = int(listOfstrings[0]) * int(listOfstrings[3]) + int(listOfstrings[2]) * int(listOfstrings[1])
        Delitel = int(listOfstrings[1]) * int(listOfstrings[3])
        nok = NOK(Delimoe,Delitel)
        return str(Delimoe // nok) + '/' + str(Delitel // nok)
    elif operation == '*':
        Delimoe = int(listOfstrings[0]) * int(listOfstrings[2])
        Delitel = int(listOfstrings[1]) * int(listOfstrings[3])
        nok = NOK(Delimoe,Delitel)
        return  str(Delimoe // nok) + '/' + str(Delitel // nok)
    else:
        return None



 
str1 = input('Введите первую дробь: ').replace(" ","")
str2 = input('Введите вторую дробь: ').replace(" ","")
# #demo
# str1 = '5 / 7'
# str2 = '4 / 8 '

try:
    print(str1,' + ',str2,'  = ',summOrProizvDrob(str1 , str2 , '+'))
    print(str1,' * ',str2,'  = ',summOrProizvDrob(str1 , str2 , '*'))
except Exception as error:
    print('Caught this error: ' + repr(error))

print('Проверка с помощью модуля fractions')

s = str1.replace(" ","").split('/')
s2 = str2.replace(" ","").split('/')
f1 = fractions.Fraction(int(s[0]) , int(s[1]))
f2 = fractions.Fraction(int(s2[0]) , int(s2[1]))
print(str1,' + ',str2,'  = ', f1 + f2)
print(str1,' * ',str2,'  = ', f1 * f2)