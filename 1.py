# ? print() выводит данные на экран
print("Hello world!") # двойные кавычки
print('Hello world!') # одинарные кавычки
print(2026) # 2026
print (2026 + 4) # 2030
print("Итого:", 500, "руб")

# комментарий

# ? переменная
name = "Алекс"
print("Воин", name)
print(f"Воин {name}")

num1 = 5
num2 = 10
total = num1 + num2
print(total)

# ? меняем значение
num = 5
print(num)
num = 10
print(num)

# ? Правила наименования переменных
# ! Только латинские символы от a-z A-Z
# ! Цифры, но не на первой позиции
# ! Разрешен символ _
# ! Нельзя использовать зарезервированные имена

# ? snake_case - рекомендован
client_name = "Иван"
ticket_price = 200

# ? camelCase
clientName = "Иван"
ticketPrice = 200


# Типы данных - у каждого своё предназначение
# integer / int / целое число
my_int = 10
print(my_int, type(my_int))


# float / float / дробное число
my_float = 10.5
print(my_float, type(my_float))


# string / str / строка
my_str_1 = 'Hello1'
print(my_str_1, type(my_str_1))
my_str_2 = "Hello2"
print(my_str_2, type(my_str_2))
my_str_3 = "Иван сказал: '...'"
print(my_str_3, type(my_str_3))
my_str_4 = 'Иван сказал: "..."'
print(my_str_4, type(my_str_4))


# int - переводит в числовый тип данных
str_in_int = int('5')
print(str_in_int, type(str_in_int))

str_in_int = int(5.0)
print(str_in_int, type(str_in_int))

str_in_int = int('привет') # ошибка


# str - переводит в строковый тип данных
int_in_str = str(5)
print(int_in_str, type(int_in_str))