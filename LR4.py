# 4 ЛР
#Для настольной игры используются карточки с номерами от 1 до . Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
#Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N ).
#Программа должна вывести номер потерянной карточки.
#Массивами и аналогичными структурами данных пользоваться нельзя.

#просуммируем все слагаемые,затем вычтем известные
n = int(input('Введите N:'))
sum = 0
for i in range(1, n + 1):
    sum += i
print('Введите номера оставшихся карточек :')
for i in range(n - 1):
    sum -= int(input())
print('Потерячнная карточка:',sum)