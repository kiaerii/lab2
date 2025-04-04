#2
a=(input('первое число'))
b=(input('второе число'))
c='abcdefghijklmnopqrstuvwxyz'
if b!='0' and (a not in c) and (b not in c):
    print(int(a)/int(b))
else:
    print('Ошибка')
