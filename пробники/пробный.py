# s = "457 567 45 136 123 247 126".split()
# g = "AB AF FD AD FE DC BC EC EG BG".split()

# from itertools import permutations
# print(*range(1, 8))
# for i in permutations("ABCDEFG"):
#     if all(str(i.index(x) + 1) in s[i.index(y)] for x, y in g):
#         print(*i)

# for m in 0,1 :
#     for e in 0,1:
#         for a in 0, 1:
#             for n in 0,1:
#                 if (e and (not m)) or (m == a) or (not n):
#                     continue
#                 else:
#                     print(n, a, m, e)


# def to4(n):
#     s = ""
#     while n > 0:
#         s = str(n % 4) + s
#         n //= 4
#     return s


# def r(n):
#     n4 = to4(n)
#     if n % 4 == 0:
#         n4 += n4[-2:]
#     else:
#         s = sum(map(int, n4))
#         s4 = to4(s)
#         n4 += s4
#     return int(n4, 4)

# print(r(7), r(15))
# for i in range(1, 1000):
#     R = r(i)
#     if R > 870 and R % 2 == 0:
#         print(R)
#         break


# from turtle import *

# tracer(0)
# m = 15
# left(90)

# lt(315)
# for i in range(3):
#     lt(315); fd(10 * m); lt(315)
# lt(45)
# fd(15*m)
# lt(270)
# fd(25*m)
# lt(270)
# for i in range(2):
#     fd(15*m); lt(270)

# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x *m , y*m)
#         dot(5, 'pink')
# done()

# print(25*15 + 100)

# size_bez_h = 24000 * 48 * 4 * (48 * 60 + 56)
# for h_size in range(1000000):
#     full = size_bez_h + 17 * (h_size * 1024 * 8)
#     if full / 1024 / 1024 / 8 > 2414:
#         print(h_size)
#         break

# from itertools import permutations
# c = 0
# for i in permutations('0123456789a', 7):
#     s = ''.join(i)
#     if s[0] != '0':
#         for i in '02468':
#             s = s.replace(i, 'x')
#         if 'xa' not in s and 'ax' not in s:
#             c += 1

# print(c)

# c = 0
# for i in open('9.txt'):
#     row = list(map(int, i.split()))
#     r3 = [i for i in row if row.count(i) == 3]
#     r2 = [i for i in row if row.count(i) == 2]
#     r1 = [i for i in row if row.count(i) == 1]
#     if len(r3) == 3 and len(r2) == 2 and len(r1) == 2:
#         if sum(r3 + r2) * 3 >= r1[0] * r1[1]:
#             c += 1

# print(c)
# from math import *
# l = 517
# kod = 13 + 8180
# one = ceil(ceil(log2(kod)) * l / 8) # byte
# print(one)
# print(one * 14892716 / 1024 / 1024 / 1024)

# from ipaddress import ip_address, ip_network

# net = ip_network("98.71.254.171/255.255.248.0", 0)
# good = []
# for i in net.hosts():
#     bi = f"{i:b}"
#     if bi.count("1") % 3 == 0:
#         good.append(i)
# print(min(good), sum(i for i in min(good).packed))

# for i in range(1, 38):
#     first = 4 * 37 ** 6 + 11 * 37 ** 5 + 3 * 37 ** 4 + i * 37 ** 3+ 1 * 37 ** 2+ 12 * 37 ** 1 + 7 * 37 ** 0
#     second = 5 * 37 ** 6 + i * 37 ** 5 + 16 * 37 ** 4 + 8 * 37 ** 3 + 3 * 37 ** 2 + 15 * 37 ** 1 + 7 * 37 ** 0

#     if (first + second) % 36 == 0:
#         print((first + second) / 36)

# def f(x, y):
#     return (x * y + 2 * x * y > a) or (x > y) or (2717 > x)

# a = 22146266

# print(all(f(x, y) for x in range(10000) for y in range(10000)))

from functools import lru_cache


@lru_cache(1000)
def f(n):
    if n >= 1100:
        return n
    else:
        return f(n + 4) * (n - 4)
    
print((f(1000) // 12 - 73 * f(1004)) // f(1008))


# c = m = 0
# nums = list(map(int, open("17.txt")))
# max36 = max([i for i in nums if abs(i) % 100 == 36])
# for tri in zip(nums, nums[1:], nums[2:]):
#     zn4 = [i for i in tri if len(str(abs(i))) == 4]
#     if len(zn4) <= 2 and sum(tri) <= max36:
#         c += 1
#         m = max(sum(tri), m)
# print(c, m)


# def f(s, m):
#     if s >= 216:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = [
#         f(s + 1, m - 1),
#         f(s + 4, m - 1),
#         f(s * 3, m - 1),
#     ]
#     if m % 2 == 0:
#         return all(h)
#     return any(h)


# print([s for s in range(1, 216) if not f(s, 2) and f(s, 4)])

# def f(n, m):
#     if n > m: return 0
#     if n == m: return 1
#     dec = int(str(n)[-2])
#     ed = int(str(n)[-1])
#     if dec < ed:
#         swap = int(str(n)[:-2] + str(ed) + str(dec))
#         print(n, swap)
#         return f(n + 2, m) + f(swap, m)
#     return f(n + 2, m)

# print(f(211, 221) * f(221, 256))

# from fnmatch import fnmatch


# def mult(n):
#     m = 1
#     c = 0
#     for i in str(n):
#         m *= int(i)
#     return m


# def check(m):
#     c = 0
#     for i in str(m):
#         if int(i) % 2 == 0:
#             c += 1
#     return c


# for i in range(0, 10**9, 4321):
#     m = mult(i)
#     if fnmatch(str(i), "3*4*56?7") and check(m) >= 4:
#         print(i, m)

# from turtle import *
# from math import dist
# from random import random

# with open("27a.txt") as f:
#     dataA = []
#     for i in f:
#         s = i.split()
#         dataA.append([float(s[0]), float(s[1]), s[2][0] + s[2][2:]])

# with open("27b.txt") as f:
#     dataB = []
#     for i in f:
#         s = i.split()
#         dataB.append([float(s[0]), float(s[1]), s[2][0] + s[2][2:]])


# def draw(clus):
#     m = 5
#     tracer(0)
#     up()
#     for cl in clus:
#         col = (
#             random(),
#             random(),
#             random(),
#         )
#         for i in cl:
#             x = float(i[0])
#             y = float(i[1])
#             goto(x * m, y * m)
#             dot(5, col)
#     done()


# def dbscan(data, r=1):
#     clusters = []
#     while data:
#         cl = [data.pop(0)]
#         for p in cl:
#             sosedi = [i for i in data if dist(i[:2], p[:2]) <= r]
#             for s in sosedi:
#                 cl.append(s)
#                 data.remove(s)
#         clusters.append(cl)
#     print(len(clusters))
#     return clusters


# def find_cen(cl):
#     m = []
#     for p in cl:
#         l = 0
#         for p2 in cl:
#             l += dist(p[:2], p2[:2])
#         m.append([l, p])
#     return min(m)[1]


# clA = dbscan(dataA)
# clB = dbscan(dataB)

# clA.sort(key=len)
# cenmaxA = find_cen(clA[1])
# cenminA = find_cen(clA[0])

# need = "BIV"
# A1 = 0
# for star in clA[1]:
#     if star[-1] == need and star[0] > cenmaxA[0]:
#         A1 += 1
# print("A1", A1)
# print("A2", int(abs(cenmaxA[1] - cenminA[1]) * 10000))

# need = "MV"
# clB.sort(key=len)
# cenminclB = find_cen(clB[0])


# def vne_kv(x, y):
#     x1 = cenminclB[0]
#     y1 = cenminclB[1]
#     if x < (x1 - 0.35) or x > (x1 + 0.35) or y > (y1 + 0.35) or y < (y1 - 0.35):

#         return True


# B1 = 0
# for star in clB[0]:
#     x = star[0]
#     y = star[1]
#     if star[-1] == need and vne_kv(x, y):
#         B1 += 1

# print("B1", B1)

# B2 = 0
# need2 = "GI"

# for cl in clB:
#     curd = [i for i in cl if i[-1] == need2]
#     for p in curd:
#         for p2 in curd:
#             B2 = max(abs(p[0] - p2[0]), B2)
# print("B2", int(B2 * 10000))
