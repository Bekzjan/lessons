# users = {
#     'name':'Aibek'

# }

# try:
#     print(users['age'])

# except KeyError as e:
#     print('Мы отловили KeyError ', e)
# except NameError as e:
#     print('Вы не создали переменную', e)

# else:
#     print('all ok! 200')
# finally:
#     print('Обработка ошибок завершено!')



# zero_except = 0

# while True: 
#     try:
#         print(eval(input('>>>')))
#     except ZeroDivisionError as e:
#         zero_except += 1
#         print('Вы пытаетесь делить на ноль')
#         print('Больше непытайтесь! или мы вас забаним!')
    
#     except TypeError as e:
#         print('Вы пытаетесь работать с разными типапи данных!',e)
    
#     except KeyboardInterrupt as e:
#         print('\nВы останавили операцию')

#     if zero_except == 3:
#         print('мы забанали вас из за ZeroDivisionError')
#         print('Вы уже поделили 3 раза')
#         break

#Problem1
import random


# random_num = random.randint(1,10)

# try:
#     user_guese = int(input('угадайте число от 1 до 10: '))
#     if user_guese == random_num:
#         print('Well done')

#     else:
#         print('not Well done. Your number was', random_num)

# except ValueError:
#     print('Ошибка: Введите целок число!')

#Problem2

# s = [1,2,3,4,5,6,7,8,9,10]
# random_number = random.randint(1,10)
# print(random_number)

#Problem3


# random_number = random.randint(1,1001)
# try:
#     user_random = int(input('Введите рандомное число: '))
#     if user_random < random_number:
#         print('Слишком мало')
#         print(random_number)
#     elif user_random > random_number:
#         print('Слишком много!')
#         print(random_number)
#     else:
#         print('')
        

# except ValueError:
#     print('Ошибка: Не целое число!')

#Problem4

# try:
#     a = [1,23,435,236,2,62,2,69,65,61,351,2,6,327,235,828,458,285,846,845]
#     random_number = random.choice(a)
#     print(random_number)

# except ValueError:
#     print('Ошибка: Не целое число!')

#problem5
# def coordinates():
#     x = random.random()
#     y = random.random()
#     print(f" x = {x}, y = {y}")

# coordinates()

#problem6

# def random_element(bek):
#     try:
#         random_element = random.choice(bek)
#         print("Случайный элемент:", random_element)
#     except IndexError:
#         print("Список пуст.")
#     except TypeError:
#         print("Несовместимый тип данных в списке.")

# data_list = [1, "Hello", [1, 2, 3], {"name": "Alice"}, 3.14]

# random_element(data_list)


#problem 8

# def random_numbers(a):
#     try:
#         random_numbers == random.randint(1,a)
#         print('Случайное число:', random_numbers)
#     except ValueError:
#         print('Некоректное число',random_numbers)

#problem9
# def generate_random_string(length):
#     random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#     print("Случайная последовательность символов:", random_string)
# input_length = input("Введите длину последовательности: ")
# try:
#     length = int(input_length)
#     if length &lt;= 0:
#         raise ValueError
#     generate_random_string(length)
# except ValueError:
#     print("Некорректная длина. Введите положительное число.")
#problem10
# def convert_to_number(string):
#     try:
#         number = int(string)
#         print("Преобразованное число:", number)
#     except ValueError:
#         print("Невозможно преобразовать в число.")

# string_list = ["123", "456", "789", "abc", "def"]
# random_element = random.choice(string_list)
# convert_to_number(random_element)















