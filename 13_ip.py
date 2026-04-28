# библиотека для работы с ip адресами
from ipaddress import *

# конвертирует текст в объект ip_address
ip = ip_address('16.16.128.0')

# формирует все ip адреса по заданному ip и маске
net = ip_network('172.16.128.0/255.255.255.128')
net = ip_network('172.16.128.0/7', False)

# Широковещательным адресом называется специализированный адрес, в котором на месте нулей в маске стоят единицы.
# Адрес сети называется специализированный адрес, в котором на месте нулей в маске стоят нули.
# Адрес сети и широковещательный адрес не могут быть использованы для адресации сетевых устройств.

print(*net.hosts())
print(max(net.hosts()))
print(min(net.hosts()))

# двоичное представление ip адреса с добавлением ведущих нулей до 32х позиций
bin_ip = f'{int(ip):032b}'

# 1 тип  - основной
'''
from ipaddress import *

net = ip_network('172.16.128.0/255.255.255.240')

cnt = 0
for ip in net:
    bin_ip = f'{int(ip):032b}'
    if bin_ip.count('1') % 2 != 0:
        cnt += 1

print(cnt)
'''


# 2 тип - основной КомпЕГЭ 28934
# hosts - универсальная. Также объяснить про 2 занятых ip адресов

from ipaddress import ip_network

net = ip_network('191.89.109.206/255.255.224.0', False)

print(max(net.hosts()))



# 3 тип - авторская
# from ipaddress import *
#
# ip_1 = ip_address('112.117.107.70')
# ip_2 = ip_address('112.117.121.80')
#
# for mask in range(12, 30)[::-1]:
#     net = ip_network(f'{ip_1}/{mask}', False)
#     if ip_1 in net.hosts() and ip_2 in net.hosts():
#         print(net.netmask)
#         break


# 4 тип - авторская КомпЕГЭ 18487

# from ipaddress import ip_address, ip_network
#
# def f(ip):
#     return f'{int(ip):032b}'.count('1') > 15
#
# for A in range(256):
#     ip = ip_address(f'192.214.{A}.184')
#     net = ip_network(f'{ip}/27', False)
#     if ip in net.hosts() and all(f(i) for i in net):
#         print(A)
#         break