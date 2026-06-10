from itertools import product 
# c = 0 
# for x in product('ГЕПАРД', repeat = 5):
#     if x.count('Г') == 1 and x[0] != 'А' and x[-1] != 'Е':
#         c += 1
# print(c)

# c = 0
# for i in product('ВИШНЯ', repeat=6):
#     if i.count('В') <= 1 and i[0] != 'Ш' and i[-1] in 'ВШН':
#         c += 1
# print(c)

# c = 0 
# for z in product('ДГИАШЭ', repeat = 5):
#     if z[0] not in 'ИАЭ' and z[-1] not in 'ДШГ':
#         c += 1
# print(c)
# c = 0 

# for i in product('01234', repeat=6):
#     if i[0] not in '01' and i[-1] not in '34':
#         c += 1

# print(c)

# c =0 
# for i in product('0123456', repeat=5):
#     if i[0] in '246' and int(i[-1]) >= 3 and i.count('4') <= 1:
#         c += 1
# print(c)

# from string import printable
# c = 0 
# for i in product(printable[:15], repeat = 5):
#     if i[0] != '0' and i.count('8') == 1 and sum(i.count(k) for k in 'abcde') >= 2:
#         c += 1
# print(c, printable[:15])

k = 0
for i in product('01234567', repeat=5):
    s = ''.join(i)
    s = s.replace('3', '1').replace('5', '1').replace('7', '1')
    if i[0] != '0' and i.count('6') == 1 and '16' not in s and '61' not in s:
        k += 1
print(k)
c = 0
for i in product('0123456', repeat=6):
    s = ''.join(i)
    if s.count('6') == 1 and s[0] != '0': 
        s = s.replace('4', '2').replace('6', '2').replace('0', '2')
        s = s.replace('3', '1').replace('5', '1')
        if '212121' == s or '121212' == s:
            c += 1

print(c)


