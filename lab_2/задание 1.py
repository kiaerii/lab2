#1
with open('data.txt','w')as f:
    f.write('11\n22\n33\n44\n55\n66\n77\n88\n99\n12')
    f.close()
with open('data.txt')as f:
    a=[int(line) for line in f]
print(a)
su=sum(a)
sr=sum(a)/len(a)
ma=max(a)
mi=min(a)
with open('result.txt','w')as f:
    f.write(f'Сумма:{su}\n')
    f.write(f'Среднее:{sr}\n')
    f.write(f'Максимум:{ma}\n')
    f.write(f'Минимум:{mi}\n')
