s=[a for a in range(1,21)]
print(s)
chetn=list(filter(lambda x: (x%2==0), s)) #оставляем четные
plus10=list(map(lambda x: x+10, s)) #увеличиваем на 10
obr=sorted(s, key=lambda x: x, reverse=True) #обратный порядок
print(chetn)
print(plus10)
print(obr)
