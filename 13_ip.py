# библиотека для работы с ip адресами
from ipaddress import *

# конвертирует текст в объект ip_address
ip = ip_address('16.16.128.0')

# формирует все ip адреса по заданному ip и маске
net = ip_network('172.16.128.0/255.255.255.128')
net = ip_network('172.16.128.0/7', False)

# двоичное представление ip адреса с добавлением ведущих нулей до 32х позиций
bin_ip = f'{int(ip):032b}'

# 1 тип
'''
from ipaddress import *

net = ip_network('172.16.128.0/255.255.255.240')

cnt = 0
for ip in net:
    bin_ip = f'{int(ip):032b}'
    if ip.count('1') % 2 != 0:
        cnt += 1

print(cnt)
'''

# 2 тип
from ipaddress import *

ip_1 = ip_address('112.117.107.70')
ip_2 = ip_address('112.117.121.80')

for mask in range(12, 30)[::-1]:
    net = ip_network(f'{ip_1}/{mask}', False)
    if ip_1 in net.hosts() and ip_2 in net.hosts():
        print(net.netmask)
        break



