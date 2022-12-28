import time


message = 'Внести время ПРИХОДА - введите 0\nВнести время УХОДА- введите 1'

time_arrival = ''
time_dipart = ''

print(message)
a = int(input())

if a == 0: 
    #print('Введите время прихода в формате 00:00 или введите now')
    time_arrival = input('Введите время прихода в формате 00:00 или введите now\n')

    if time_arrival == 'now':
        time_arrival = time.strftime("%m/%Y, %H:%M:%S", time.time())
    
if a == 1: 
    #print('Введите время ухода в формате 00:00 или введите now')
    time_dipart = input('Введите время ухода в формате 00:00 или введите now\n')

    if time_dipart == 'now':
        time_dipart = time.time()

print(time_arrival)
print(time_dipart)

