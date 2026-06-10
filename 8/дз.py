from itertools import permutations, product

c = 0
for i in product("012345678", repeat=7):
    if i[0] not in "01357" and int(i[-1]) % 3 != 0 and i.count("6") >= 1:
        c += 1
print(c)


c = 0
for i in product("01234", repeat=5):
    s = "".join(i)
    if i[0] != "0":
        for k in "024":
            s = s.replace(k, "*")

        if s.count("*") <= 3:
            c += 1
print(c)

c = 0
from string import printable

for i in product(printable[:12], repeat=6):
    s = "".join(i)
    if s.lower().count("b") == 1 and s[0] != "0":
        for i in "13579B":
            s = s.replace(i.lower(), "*")
        for i in "02468A":
            s = s.replace(i.lower(), "+")
        if s.count("*") == s.count("+"):
            c += 1
print(c)

c = 0
for i in product('0123456', repeat=6):
    s = ''.join(i)
    if s.count('6')==1 and s[0]!='0':
        s = s.replace('2', '0').replace('4', '0').replace('6', '0')
        s = s.replace('3', '1').replace('5', '1')
        if '00' not in s and '11' not in s:
            c += 1

print(c)
from string import printable
c = 0
for i in product(printable[:15], repeat=5):
    if i[0] != '0' and i.count('8') == 1 and sum(i.count(k) for k in printable[10:15]) >= 2:
        c += 1

print(c)


c = 0

for i in product("012345", repeat=6):
    if i.count("2") == 1 and i[0] != "0":
        s = "".join(i)
        for i in "135":
            s = s.replace(i, "*")

        if "*2" not in s and "2*" not in s:
            c += 1

print(c)
c = 0
from string import printable

for i in product(printable[:16], repeat=4):
    if i[0] != "0" and i.count("3") == 1:
        s = "".join(i)
        for i in printable[:16]:
            s = s.replace(i * 2, "*")
        if s.count("*") == 0:
            c += 1

print(c)


c  = 0

k = 0
for i in product(sorted('ПЛЮШКА'), repeat=5):
    k += 1
    s = ''.join(i)
    if i.count('Ю') <= 1 and 'ШШ' not in s:
        c =k

print(c)

c = 0
k = 0
for i in product(sorted("МИЗАНТРОП"), repeat=5):
    k += 1
    s = "".join(i)
    if k % 2 == 0 and s[0] == "Н" and s.count("Р") == 2:
        c = k
print(c)

c = 0
k = 0
for i in product(sorted("ТЕОРИЯ"), repeat=6):
    k += 1
    if k % 2 == 1 and i[0] not in "РТЯ" and i.count("И") >= 2:
        c = k
print(c)
c = 0 
k =0 
for i in product(sorted('МИНУС'), repeat=4):
    k += 1
    s = ''.join(i)
    for i in 'МНС':
        s = s.replace(i, 'x')
    for i in 'ИУ':
        s = s.replace(i, 'c')
    
    if s.count('x') >= s.count('c'):
        c = k

print(c)

word = 'АЛГОРИТМ'
k = 0 
c =0 
for i in product(sorted(word), repeat=5):
    k += 1
    s = ''.join(i)
    if k % 2 == 0 and s[0] not in 'АГ' and s.count('Р') >= 2:
        print(k)
        break

