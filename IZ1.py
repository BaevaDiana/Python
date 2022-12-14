# ИЗ1.
#Задание 6.
#Дана последовательность,которая состоит из пар натуральных чисел.
#Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма всех выбранных чисел имела такой же остаток от деления на 7, как наименьшая возможная, и при этом была максимальной возможной.
#Гарантируется, что искомую сумму получить можно.
#Программа должна напечатать одно число – максимальную возможную сумму, соответствующую условиям задачи.

inf = open('6a.txt',"r")
n = int(inf.readline())
s = {0:0}
min_s = 0#минимальная возможная сумма
mod = 0 #остаток при делении
for i in range(n):
    p = list(map(int,inf.readline().split()))
    min_s += min(p)#выбираем минимум из списка p,в котором у нас находятся считанная пара,т.е. находим минимальное число из пары
    sums = [s[j] + k for j in s for k in p]#формируем все возможные суммы
    s = {x % 7 : x for x in sorted(sums)}#составляем словарь, в котором ключем выступает остаток от деления на 7, а значения это упорядоченные по возрастанию все возможные суммы
mod = min_s % 7 # вычисляем остаток от деления на 7 минимально возможной суммы
print(s[mod])
inf.close()




