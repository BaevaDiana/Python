# 5 ЛР
#Дана строка. Замените в этой строке все появления буквы h на букву H, кроме первого и последнего вхождения.

s=input('Введите строку:')
k=s.count('h')#cчитаю количество h
s1=s.replace('h','*',1)
s2=s1.replace('h','H',k-2)
s3=s2.replace('*','h',1)
print('Преобразованное слово:',s3)