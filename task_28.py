"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
2 2
4
"""

numberA = int(input("Введите число A: "))
numberB = int(input("Введите число B: "))


def sum(a, b):
    result = 0
    if a > 0:
        result += 1 + sum(a - 1, b)
          
    elif b > 0:
        result += 1 + sum(0, b - 1)
         
    return result
    
   
        

print(sum(numberA, numberB))