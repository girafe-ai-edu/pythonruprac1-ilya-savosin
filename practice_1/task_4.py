# -*- coding: utf-8 -*-
"""
Разработайте программу, запрашивающую у  пользователя целое четырехзначное число и подсчитывающую сумму составляющих его цифр. Например, если пользователь введет число 3141,
 программа должна вывести 
следующий результат: 3 + 1 + 4 + 1 = 9

@author: Savant
"""
string_of_number = input('Введите целое четырёхзначное число: ')

digits = list(string_of_number)
number = int(string_of_number)
sum_of_digits = number % 10 + number // 10 % 10 + number // 100 % 10 + number // 1000
print(" + ".join(digits), '=', sum_of_digits)