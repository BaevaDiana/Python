# 11 ЛР
# Дана база данных о продажах некоторого интернет-магазина.
# Каждая строка входного файла представляет собой запись вида Покупатель товар количество,
# где Покупатель – имя покупателя (строка без пробелов),
# товар – название товара (строка без пробелов),
# количество – количество приобретенных единиц товара.
# Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.
# Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.

from collections import defaultdict #создаём стандартный словарь
from sys import stdin

dict = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    name, thing, quan = map(str, line.split())
    dict[name][thing] += int(quan)

for name in sorted(dict):
    print(name + ":")
    for thing in sorted(dict[name]):
        print(thing, dict[name][thing])