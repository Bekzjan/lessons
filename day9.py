
cities = []
while True:
    action = int(input("Выберите действие: \n"
        " 1. Добавить новый город \n"
        " 2. Отобразить список городов \n"
        " 3. Заменить город \n"
        " 4. Удалить город \n"
        " 5. Посетить следующий город \n"
        " 6. Выход \n"))
    if action == 6:
        print("Программа завершает работу!")
        break
    elif action == 1:
        city = input("Введите название города: ")
        if cities == city:
            print(f"б. Такой город уже есть!, {cities[city]}")
        elif city.isdigit() == True:
            print("в. Некорректное название!")
        else:
            cities.append(city)
            print("a. Город добавлен!")
    elif action == 2:
        if cities == []:
            print("Нет городов для вывода, заполните лист!")
        else:
            print(f"Список городов: \n", cities)
    elif action == 3:
        if cities == []:
            print("Нет городов для изменения, заполните лист!")
        else:
            choice = int(input(f"Выберите город по номеру для замены (счет начинается с 0):{cities}: "))
            city = input("Введите новый город: ")
            print(f"Новый город: {city}")
            if city != cities:
                cities[choice] = city
                print("б. Город заменен")
            elif cities[choice] == city:
                print(f"в. Такой город уже есть! {city} - 3")
            elif city.isdigit() == True:
                print("г. Некорректное название!")
    elif action == 4:
        if cities == []:
            print("Нет городов для удаления, заполните лист!")
        else:
            choice2 = int(input(f"Выберите город по номеру для удаления (счет начинается с 0):{cities}: "))
            city = input("Введите название города, который вы хотите удалить: ")
            if city != cities[choice2]:
                print("а. Текущий город отсутвует")
            elif city.isdigit() == True:
                print("б. Некорректное название!")
            elif city == cities[choice2]:
                cities.pop(choice2)
                print("в. Город удален!") 
    elif action == 5:
        if cities == []:
            print("Нет городов для выбора, заполните лист!")
        else:
            city_choice = int(input(f"В каком городе вы хотите находится в данный момент? (счет начинается с 0) {cities}: "))
            print(f"На данный момент мы находимся в городе: {cities[city_choice]}")
            choice3 = int(input(f"Выберите, какой город вы хотите посетить следующим? (счет начинается с 0):{cities}: "))
            city = input("Введите название города, который вы хотите Посетить: ")
            if city == cities[choice3]:
                print(f"а. Сейчас мы находися в городе: {cities[choice3]}")
            elif city.isdigit() == True:
                print("б. Некорректное название!")
            elif city != cities[choice3]:
                print("в. Вы выбрали разные значения пары значение/название!")