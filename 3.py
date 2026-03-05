# ? boolean / bool / логический тип
my_bool_1 = True
print(my_bool_1, type(my_bool_1))
my_bool_2 = False
print(my_bool_2, type(my_bool_2))


# ? логические операторы
print(5 > 3) # * больше
print(5 >= 3) # * больше и равно
print(5 < 3) # * меньше
print(5 <= 3) # * меньше и равно
print(5 == 3) # * равно
print(5 != 3) # * не равно


# ? условные операторы / if-elif-else
# * 1. if (если)
num = 10
if num > 0:
    print("Число положительное")
# * 2. Конструкция if-else (если-иначе)
age = 15
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")


# ? Конструкция if-elif-else (если - иначе если - иначе)
traffic_light = "yellow"
if traffic_light == "green":
    print("Едем")
elif traffic_light == "yellow":
    print("Ждем")
else:
    print("Стоим")


# ? составные выражения / (and, or)


# * Оператор and (И) Выражение истинно, только если ОБА условия верны
age = 25
balance = 1000
if age >= 18 and balance > 500:
    print("Покупка разрешена")
else:
    print("Недостаточно средств или мал возраст")


# * 2. Оператор or (ИЛИ) Выражение истинно, если ХОТЯ БЫ ОДНО из условий верно
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("Сегодня выходной")
else:
    print("Сегодня рабочий день")


# * Оператор not (НЕ) Инвертирует (переворачивает) результат условия
is_banned = False
if not is_banned:
    print("Доступ разрешен. Вы не забанены.")
else:
    print("Доступ к ресурсу запрещен.")


# ? вложенные конструкции / nested structures
username = "admin"
password = "1234"
if username == "admin":
    print("Логин найден.")
    if password == "1234":
        print("Пароль верный. Вход выполнен!")
    else:
        print("Неверный пароль.")
else:
    print("Такого пользователя не существует.")


# ! Важно помнить порядок выполнения (приоритет):
# * not (выполняется первым)
# * and (выполняется вторым)
# * or (выполняется последним)
# * Скобки () меняют этот порядок.


# ? задачи
x,y,z = True, False, True
print(x or y and z)
print(x and y or x)
print(not x or y and z)
print(not x and not y or z)
print(x and x or y and x or x)
print((x or y) and (not z))