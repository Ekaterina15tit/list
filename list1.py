n = int(input ('Кол-во чисел: '))
list = []

for i in range (n):
    a = int(input ('Введите число больше 1, но меньше 10 000: '))
    if a>=1 and a<=10000:
        list.append (a) 
    else:
        print ('Введите другое значение: ')
print(list)
print(list[::-1]) #переворачиваем  массив 