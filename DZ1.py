# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def whatIsThisNumber(number):
    thisNumber = ''
    if number == None:
        return -1
    if number < 0:
        return -1
    elif number <10:
        return str(number)
    match number:
        case 10:
            thisNumber = 'A'
        case 11:
            thisNumber = 'B'
        case 12:
            thisNumber = 'C'
        case 13:
            thisNumber = 'D'
        case 14:
            thisNumber = 'E'
        case 15:
            thisNumber = 'F'
    return thisNumber

def transformationIn16(number , sustem): # Система 16-чная
    result = 0
    ost = 0
    rezString = ''
    if number < 0:
        number *= -1
        operand = '-'
    else:
        operand = ''

    if number < sustem:
        return operand + whatIsThisNumber(number)
    
    while True:
        result = number // sustem
        ost = number % sustem
        if result < sustem:
           rezString = rezString  + whatIsThisNumber(ost) + whatIsThisNumber(result) 
           break
        else:
           number = result
           rezString = rezString + whatIsThisNumber(ost)
    return operand + rezString[::-1]

num = int(input('Get me number:'))

print(transformationIn16(num , 16))
print(format(num,'X'))
print(transformationIn16(num , 16) == format(num,'X'))