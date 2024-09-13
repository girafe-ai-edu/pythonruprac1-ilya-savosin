# -*- coding: utf-8 -*-
"""
Напишите программу для расчета индекса массы тела (body mass index – 
BMI) человека. Пользователь должен ввести свой рост и вес, после чего вы 
используете одну из приведенных ниже формул для определения индекса.
BMI = вес/рост**2 
"""
weight = input('Введите Ваш вес в кг: ')
height = input('Введите Ваш рост в м (например, 1.73): ')

print(f"BIM = {float(weight) / float(height) ** 2:.1f} кг/м2")

