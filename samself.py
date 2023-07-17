# problem 1
# for i in range(1,11):
#     print(i)

# problem 2
# words = ['bmw','mers','subaru','suzuki','lexus']

# for i in words:
#     if len(i) > 5:
#         print(i)
# problem 3
# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print("Good")
# else:
#     print("Not good")
# Problem 4
# str = input("Введите слово: ")
# reversed_str = "".join(reversed(list(str)))
# print(reversed_str)
# problem 5
# num = [12,45,65,23,77,89,45,36,11,13,14,17]
# for i in num:
#     if i % 3 == 0:
#         print(i)
# 6
# text = input('Введите слово: ')

# if text == text[::-1]:
#     print("This is palindrom!")
# else:
#     print("This is not palindrom!")
# 7
# text = input("введите предложение: ")

# print(text.upper())

# 8


# for i in range(1,21):
#     if i % 2 == 0 and i % 3 != 0:
#         print(i)

# 9
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

#10
# text = input("Введите предложение: ")

# text = text.split(" ")
# for i in text:
#     print(i)

#11
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]

# for i in words:
#     if i == i[::-1]:
#         print(i)
#12
# list = []
# sum = 0

# for i in range(1,1001):
#     if i % 3 == 0 and i % 5 == 0:
#        sum += i
#        print(sum) 

#13
# str = "4729461084"
# sum = 0


# for i in str:
#     sum += int(i)
#     print(sum)    

#14
# a = float(input("Введите число 1: "))
# b = float(input("Введите число 2: "))
# operations = input("Введите операцию( + , - , * , /, % ) ")

# if operations == "+":
#     print(a + b)
# elif operations == "-":
#     print(a - b)
# elif operations == "*":
#     print(a * b)
# elif operations == "/":
#     if a == 0 or b == 0:
#         print('Error')
#     else:
#         print(a / b)
# elif operations == "%":
#     print(a * b / 100)

# else:
#     print('Error')
#15

list = []
n = int(input('Введите число: '))

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        continue
    print(i)