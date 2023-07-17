#problem1
# menu = {
#     'lagman': 120,
#     'plov': 150,
#     'borsh': 100,
#     'besh_barmak': 130
# }


# menu['besh_barmak'] = 135
# menu.remove['borsh']

# print(menu)


#problem2

# menu['drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']


# print(menu)

# #problem3

# #problem4
# user_credentials = {}

# for i in range(3):
#     username = input("Введите имя пользователя: ")
#     password = input("Введите пароль: ")
#     user_credentials[username] = password


# print(user_credentials)



#problem5
# dict ={

#     "Bekzhan" : 'programmer',
#     'Diasbek' : 'teacher',
#     'Kasym'   : 'businessman',
#     'Lamyia'  : 'stylist',
#     'Iranbek' : 'Haircutter'
# }

# for name,prof in dict.items():
#     print(f"Hello {name}, good profession {prof}")

#problem6

# data = set()

# for i in range(10):
#     number = int(input("Введите число: "))
#     data.add(number)

# print(data)





#problem 7
south_american_countries = ['Argentina', 'Brasil', 'Chili', 'Columbia', 'Surinam', 'Urugway', 'Surinam']


#problem 8


# chemodan = []

# for i in range(1, 6):
#     item = input(f"Введите {i}-й предмет: ")
#     chemodan.append(item)


# suitcase.pop()
# print(suitcase)




#problem9
# farm1 = {'корова', 'свинья', 'курица', 'лошадь'}
# farm2 = {'лошадь', 'коза', 'овца', 'курица'}

# new_set = farm1.intersection(farm2)

# print(new_set)


#problem10
farm1 = {'корова', 'свинья', 'курица', 'лошадь'}
farm2 = {'лошадь', 'коза', 'овца', 'курица'}

new_set = farm2.difference(farm1)

print(new_set)