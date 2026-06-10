from math import *

# l = 23
# kod = 10
# char = ceil(log2(kod))
# one=ceil(char*l / 8)
# print((one+20)*35)

# l = 23
# kod = 10 + 9090
# char = ceil(log2(kod))
# one = ceil(l * char / 8)
# print(23552*one/1024)

# l = 163
# kod = 1500 + 10
# one = ceil(ceil(log2(kod)) * l / 8)
# print(one * 65536 / 1024)

# kod = 26 * 2 + 10 + 450
# for l in range(10000):
#     if ceil(l * ceil(log2(kod)) / 8) * 575 >= 100 * 1024:
#         print(l)
#         break

# kod = 10 + 1234
# l = 10000
# while True:
#     one = ceil(l * ceil(log2(kod)) / 8)
#     if one * 65_536 <= 2050 * 1024:
#         print(l)
#         break
#     l -= 1

# ls = 261
# char = 0
# while True:
#     one = ceil(char * ls / 8)
#     if 252500 * one > 31 * 1024 * 1024:
#         print(2**(char-1)+1)
#         break
#     char += 1

# for n in range(1, 100000):
#     b = ceil(log2(n))
#     code = ceil(261 * b / 8)
#     if 252_500 * b > 31 * 2 ** 20:
#         print(n)


# l = 80
# for i in range(1, 100000):
#     char = ceil(log2(i))
#     one = ceil(char * l / 8)
#     if one * 1200 <= 150 * 1024:
#         print(2 ** char)

# n = 10 + 17
# l = 0
# while True:
#     l += 1
#     one = ceil(l * ceil(log2(n)) / 8)
#     if 7564230 * one > 31 * 1024 * 1024:
#         print(l)
#         break

# x = 18
# kod = 10 + 26 * 2 + 70
# one = ceil(ceil(log2(kod)) * x / 8)
# for dop in range(10000):
#     o = one + dop 
#     if 2000 * o <= 100 * 1024:
#         print(dop)

# l = 312
# c = 0
# for n in range(1, 100000):
#     char = ceil(log2(n))
#     one = ceil(l * char / 8)
#     if 51 * 1024 * 1024 < 125700 * one < 52 * 1024 * 1024:
#         c += 1
# print(c)

# l = 21
# kod = 33 * 2
# for tech in range(1, 10000):
#     f = kod + tech
#     one = ceil(l * ceil(log2(f)) / 8)
#     if 1300 * one <= 25 * 1024:
#         print(tech)

l = 24
kod = 26 * 2 + 10

for d in range(1000000):
    f = d + kod
    one = ceil(l * ceil(log2(f)) / 8 )
    if 5100 * one <= 170 * 1024:
        print(d)
    