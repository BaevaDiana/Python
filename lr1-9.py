#1 ЛР
#Дележ яблок.
#𝑛 школьников делят 𝑘 яблок поровну, неделящийся остаток остается в корзинке.
#Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
# Программа получает на вход числа 𝑛 и 𝑘 и должна вывести искомое количество яблок (два числа).
n = int(input('Число школьников = '))
k = int(input('Число яблок = '))
if n>=k:
    x1=n//k
    y1=n%k
    print('Каждому школьнику достанется яблок - ',x1)
    print('В корзине останется яблок -',y1)
elif k>n:
    x2=k//n
    y2=k-(n*x2)
    print('Каждому школьнику достанется яблок - ', x2)
    print('В корзине останется яблок -', y2)

#2 ЛР
#Минимум из двух чисел.
#Даны два целых числа. Выведите значение наименьшего из них.
x1=int(input('Введите первое число:'))
x2=int(input('Введите второе число:'))
if x1<x2:
    print('Наименьшее число:',x1)
else:
    print('Наименьшее число:', x2)

