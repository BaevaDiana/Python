# 7 ЛР
# Дан список из чисел и индекс элемента в списке k. .
# Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
# Программа получает на вход список, затем число k.
# Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.
# Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов.
# Также нельзя использовать дополнительный список. Также не следует использовать метод pop(k) с параметром.

a = []
print('Введите количество элементов в списке:')
n=int(input())
print('Введите элементы списка:')
for i in range(n):
  a.append(int(input()))
print('Введите число k:')
k=int(input())
for j in range(n-1):
  if k==j:
    a[j]=a[j+1]
  elif j>k:
    a[j]=a[j+1]
a.pop()
print('Новый массив:')
for i in range(n-1):
  print(a[i], end =' ')
