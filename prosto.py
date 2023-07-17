# import subprocess

# results =  subprocess.check_output(['netsh','wlan','show','network'])
# results = results.decode('acsii')
# results = results.replace("\r", "")
# ls  = results.split("\n")
# ls = ls[4:]
# ssids = []
# x = 0
# while x < len(ls):
#     if x % 5 == 0:
#         ssids.append(ls[x])
#     x += 1
# print(ssids)

# import threading
# def pfg():
#     print("goal gesture\n")

# timer = threading.Timer(5.0, pfg)
# timer.start
# print(timer)

# def fibonacci(n):
#     if n <= 0:
#         return "Некорректный ввод"
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         fib_list = [0, 1]
#         for i in range(2, n):
#             fib_list.append(fib_list[i-1] + fib_list[i-2])
#         return fib_list

# n = int(input("Введите количество чисел Фибоначчи: "))
# fib_sequence = fibonacci(n)
# print(fib_sequence)

#problem1
# def calculate_division(a, b):

#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return "Ошибка: деление на ноль"
#     except TypeError:
#         return "Ошибка: некорректный тип данных"

# num1 = int(input('Vvedite chislo 1: '))
# num2 = int(input('Vvedite chislo 2: '))
# division_result = calculate_division(num1, num2)
# print(division_result)


print(eval)




