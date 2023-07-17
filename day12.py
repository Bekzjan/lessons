import time, datetime
import string
from string import ascii_letters
import sys
import os
import random
from random import randint
import time
import csv

# today = datetime.date.today()
# now = datetime.datetime.now()


# print(now)
# print(today)

# now = datetime.datetime.now()
# formatted_date = now.strftime("%D")
# print(formatted_date)


# date1 = datetime(2002, 1, 29)
# date2 = datetime(2023, 7, 10)
# difference = date2 - date1
# print(difference)

# password = ''

# while len(password) < 10:
#     password += choise(ascii_letters + digits)

#     print(password)



# print(sys.platform)
# print(sys.version)
# for arg in sys.argv:
#     print(arg)

# problem 1

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# random_names = random.sample(names, 4)
# print(random_names)

#problem 2

# print(sys.version)
# print(sys.platform)


#problem 3
# operating_sys = sys.platform
# print(operating_sys)
# print(sys.argv)















#problem5
# random.shuffle(names)
# group1 = names[:3]
# group2 = names[3:6]
# group3 = names[6:9]
# group4 = names[9:]

# print("Группа 1:", group1)
# print("Группа 2:", group2)
# print("Группа 3:", group3)
# print("Группа 4:", group4)


#problem1

# for i in range(10):
#     os.system(f"touch new{randint(1,100)}.txt")

#     os.system("rm -rf *txt")

#problem2
# value1 = input("Введите значение 1: ")
# value2 = input("Введите значение 2: ")

# size1 = value1
# size2 = value2

# if size1 > size2:
#     print("Значение 1 занимает больше памяти")
# elif size1 < size2:
#     print("Значение 2 занимает больше памяти")
# else:
#     print("Оба значения занимают одинаковое количество памяти")


#problem 3
# while True:
#     n = int(input("Введите N: "))
#     password = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*',k = n))
#     print(password)


#problem 4

# while True:
#     k = ['Rock','Scissors','Paper']

#     my_choise = input('Select k(Rock,Scissors,Paper): ')
#     python_choise = random.choice(k)

#     print("Your choise: ",my_choise)
#     print("Python choise", python_choise)

#     if my_choise == python_choise:
#         print('Draw!')
#     elif (my_choise == 'Rock' and python_choise == 'Scissors') or (my_choise == 'Paper' and python_choise == 'Rock') or (my_choise == 'Scissors' and python_choise == 'Paper'):
#         print('You win')
#     else:
#         print('You lose')


#problem1
# number = random.randrange(6,13,2)
# print('Рандомное четное число: ',number)

# b = random.randrange(5,101,5)
# print('Число кратное пяти: ', b)

#problem3

# from datetime import datetime, timedelta
# current_date = datetime.now()
# future_date = current_date + timedelta(days=1000)


# print('Сегоднешняя дата:    ', current_date)
# print("Дата через 1000 дней:", future_date.strftime("%Y-%m-%d %X"))

#problem 1
# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]

# for i in range(len(numbers)-1):
#     print(numbers[i] + numbers[i+1])
#problem 2 
# from datetime import datetime

# current_time = datetime.now()
# print("Текущее время:", current_time)


#problem 3 
# for i in range(10):
#     print("Step", i+1)
#     time.sleep(1) 

#problem 4 
# list1 = [1, 3, 5, 7, 9, 11, 13]
# list2 = [2, 4, 6, 8, 10, 12, 14]

# for num1, num2 in zip(list1, list2):
#     print("Первое число:", num1)
#     print("Второе число:", num2)
