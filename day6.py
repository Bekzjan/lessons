# s = []
# for i in range(5):
#     print(i)
#     num = int(input("enter: "))
#     if num not in s:
#         s.append(num)
#     else:
#         print()

# print(s)

#1
# lang1 = 'php'
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']


# if lang1 in languages:
#     print("this language is this list")
# else:
#     print("Not in list")

#1.2
# a = []
# for i in range (1,11):
#     print(i)
#1.3
# a = []
# for i in range (1,21):
#     if i% 2 == 0:
#         print(i)
#1.4
# a = 0
# for i in range(1,101):
#     a += i
# print(a)
#1.5

# for i in range(1,11):
#     a = i * 5
#     print(a)
#1.6
# a = 1
# for i in range(1,6):
#     a *= i
#     print(a)

#1.8

# num = [1,2,3,4,5]
# sum = 0

# for i in num:
#     sum += i
#     print(sum)
#1.9------------------


#1.10
# num = [10]
# for i in range(10,0,-1):
#     print(i)
#1.11

# a = []
# for i in range(1,101):
#      if i % 3 == 0 and i % 5 == 0:
#         print(i)
      
#2
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     if i == 'php':
#         break
#     print(i)

#3
# a = 7
# for i in range(5):
#     a *= a
#     print(a)

#4-----------------
# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# for i in languages:
#     print(languages.index(i),i)
    



#6
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in names:
#     if names.index(i) % 2 == 0:
#         print(i)  

#7
# names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
# for i in names(14):
#     if names.index(i) % 2 == 0:
#         print(i)

# #8
# list = [123,456,789,234,23567,453,234,675]

# #8.1
# for i in list():
#     if 100 <= list <= 999:
#         print("Число является трёхзначным")
# else:
#     print("Число не является трёхзначным")

# #8.2
# if list > 0 and list % 2 == 0:
#     print("Число является положительным и чётным")
# else:
#     print("Число не является положительным и чётным")
# #8.3

# if list % 31 == 0:
#     print("Число делится на 31 без остатка")
# else:
#     print("Число не делится на 31 без остатка")

# #8.4
# if (list > 100 and list % 17 == 0) or (list > 150 and list == 13**2):
#     print("Число удовлетворяет условиям для показа:", list)
# else:
#     print("Число не удовлетворяет условиям для показа")


#9
count_condition_1 = 0
count_condition_2 = 0


numbers = range(-100, 101)

for number in numbers:
    
    if number % 13 == 0 and number % 2 == 0:
        number = number ** 2
        count_condition_1 += 1

    
    if number % 7 == 0 and number % 2 != 0:
        count_condition_2 += 1
        if number % 2 != 0:
            print(number)
print("Количество чисел, подходящих под первое условие:", count_condition_1)
print("Количество чисел, подходящих под второе условие:", count_condition_2)




