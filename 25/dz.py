# from fnmatch import fnmatch

# # for i in range(0, 10 ** 9, 23):
# #     if fnmatch(str(i) , '12345?7?8'):
# #         print(i, i//23)

# # for i in range(0, 10**8, 141):
# #     if fnmatch(str(i), '1234*7'):
# #         print(i, i//141)

# # for i in range(0, 10**10, 2023):
# #     if fnmatch(str(i), '1?2139*4'):
# #         print(i, i//2023)

# # for i in range(0, 10**7, 159):
# #     if fnmatch(str(i), '2?1*67'):
# #         print(i, i//159)


# # comb = []
# # from itertools import product

# # for l in range(3):
# #     for i in product("13579", repeat=l):
# #         comb.append("".join(i))

# # d = []
# # for i in "02468":
# #     for x in comb:
# #         for z in comb:
# #             num = int(f"1{x}2{i}3{z}45")
# #             if num % 153 == 0 and num <= 10**8:
# #                 d.append(num)

# # for d in sorted(d):
# #     print(d, d // 153)

# from itertools import *

# comb = []

# for l in range(4):
#     for i in product("13579", repeat=l):
#         comb.append("".join(i))

# d = []
# for a in "02468":
#     for b in comb:
#         num = int(f"1{a}2157{b}4")
#         if num % 133 == 0 and num < 10**10:
#             d.append(num)

# for i in sorted(d):
#     print(i, i // 133)

from itertools import permutations, product

# comb = []
# for l in range(4):
#     for i in product('02468', repeat=l):
#         comb.append(''.join(i))
# g = []
# for i in range(10):
#     for k in comb:
#         s = int(f'1592{k}6{i}8')
#         if s % 1996 == 0:
#             g.append(s)
# for i in sorted(g):
#     print(i, i//1996)

# comb = []
# for i in range(4):
#     for p in product(range(10), repeat=i):
#         comb.append("".join(str(x) for x in p))

# res = []
# for c in (0, 2, 4, 6, 8):
#     for i in range(10):
#         for i1 in range(10):
#             for h in (1, 3, 5, 7, 9):
#                 for c1 in (0, 2, 4, 6, 8):
#                     num = int(f"{c}9{i}23{i1}23{h}{c1}")
#                     if num % 1984 == 0 and num < 10**10:
#                         res.append(num)

# for i in sorted(res):
#     print(i, i // 1984)


# def s(n):
#     divs = find_divs(n)
#     if not divs:
#         return 0
#     return sum(i for i in divs if i % 2 == 0)

# for i in range(1204300, 1204380):
#     S = s(i)
#     if S != 0 and S % 10 == 0:
#         print(i, S)


# def find_divs(n):
#     divs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divs |= {i, n // i}
#     return sorted(divs)


# num = 250201
# c = 0
# while True:
#     divs = find_divs(num)
#     if not divs:
#         num += 1
#         continue
#     s = divs[0] + divs[-1]
#     if s % 123 == 17:
#         print(num, s)
#         c += 1
#     num += 1
#     if c == 5:
#         break


# def find_divs(n):
#     divs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divs |= {i, n // i}
#     return sorted(divs)


# def m(n):
#     d = find_divs(n)
#     if not d:
#         return 0
#     return d[0] + d[-1]


# c = 0
# for i in range(452022, 10**10):
#     M = m(i)
#     if M % 7 == 3:
#         print(i, M)
#         c += 1
#     if c == 5:
#         break


# def find_divs(n):
#     divs = set()
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             divs |= {i, n // i}
#     return sorted(divs)


# c = 0
# for i in range(150001, 200000):
#     s = sum(find_divs(i))
#     if s % 13 == 10:
#         print(i, s)
#         c += 1
#     if c == 7:
#         break


def find_divs(n):
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs |= {i, n // i}
    return sorted(divs)


# c = 0
# for i in range(350001, 400000):
#     d = find_divs(i)
#     if len(d) > 1:
#         m = d[-1] - d[0]
#         if m % 23 == 9:
#             c += 1
#             print(i, m)
#     if c == 6:
#         break

# c = 0
# for i in range(550001, 555000):
#     d = find_divs(i)
#     if d:
#         f = sum(d) // len(d)
#         if f % 31 == 13:
#             print(i, f)
#             c += 1
#     if c == 5:
#         break

# c = 0
# for i in range(500_001, 505_000):
#     d = find_divs(i)
#     en8 = [i for i in d if i % 10 == 8 and i != 8]
#     if en8:
#         print(i, min(en8))
#         c += 1
#     if c == 5:
#         break

# c = 0
# for i in range(550_001, 555_000):
#     d = find_divs(i)
#     en7 = [i for i in d if i % 10 == 7]
#     if len(en7) == 3:
#         print(i, max(en7))
#         c += 1
#     if c == 5:
#         break


# def d(n):
#     d = find_divs(n)
#     if len(d) < 6:
#         return 0
#     return d[-6]


# c = 0
# for i in range(300_000_001, 10**13):
#     dn = d(i)
#     if dn > 0:
#         print(i, dn)
#         c += 1
#     if c == 5:
#         break

# c = 0
# for k in range(1, 1000000):
#     nk = 750000 + k
#     d = find_divs(nk)
#     d.append(nk)
#     dchet = [i for i in d if i % 2 == 0]
#     if len(dchet) % 2 == 1:
#         print(k, len(dchet))
#         c += 1
#     if c == 5:
#         break

# c = 0
# for i in range(769_999, 0, -1):
#     d = [1] + find_divs(i)
#     a = sum(d) // len(d)
#     if a % 100 == 12:
#         print(i, a)
#         c += 1
#     if c == 5:
#         break

# c = 0
# for i in range(699_999, 0, -1):
#     d = find_divs(i)
#     if not d:
#         m = 0
#     else:
#         m = sum(d) // len(d)

#     if m % 1000 == 313:
#         print(i, m)
#         c += 1
#     if c == 7:
#         break

# c = 0


# def s(n):
#     d = find_divs(n)
#     if len(d) < 3:
#         return 0
#     return sum(d[-3:])


# x = []
# for i in range(10_000_001, 10**10):
#     sn = s(i)
#     if sn != 0 and int(sn**0.5) ** 2 == sn:
#         x.append([i, sn])
#         c += 1
#     if c == 5:
#         break

# for i in sorted(x, key=lambda x: x[0]):
#     print(i[1])
# c = 0
# x = []
# for i in range(1_200_000, 0, -1):
#     d = find_divs(i)
#     if len(d) > 1:
#         s = d[0] + d[1]
#         if s % 2022 == 0:
#             x.append([i, s])
#             c += 1
#     if c == 5:
#         break

# for i in sorted(x, key=lambda x: x[0]):
#     print(i[0], i[1])


# c = 0


# def p(n):
#     d = find_divs(n)
#     if len(d) < 5:
#         return 0
#     m = 1
#     for i in d[:5]:
#         m *= i
#     return m


# c = 0
# n = 200_000_000
# while True:
#     n += 1
#     pn = p(n)
#     if pn % 10 == 1 and pn < n:
#         print(pn, max(find_divs(n)[:5]))
#         c += 1
#     if c == 5:
#         break

# c = 0
# n = 900_000
# while True:
#     n += 1
#     d = find_divs(n)
#     if len(d) < 2:
#         continue
#     m = d[0] + d[-1]
#     if m % 100 == 46:
#         print(n, m)
#         c += 1
#     if c == 5:
#         break


def find_easy_m(n) -> list:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i] + find_easy_m(n // i)
    return [n]


# c = 0
# n = 1_000_000

# while True:
#     n += 1
#     divs_ez = set(find_easy_m(n))
#     if len(divs_ez) == 3:
#         print(n, max(divs_ez))
#         c += 1
#     if c == 5:
#         break


# n = 1200000
# c = 0
# while True:
#     n += 1
#     d = sorted(set(find_easy_m(n)))
#     if n in d:
#         d.remove(n)
#     if len(d) >= 2:
#         m = d[0] + d[-1]
#         if m > 2000 and m % 10 == 8:
#             print(n, m)
#             c += 1
#     if c == 5:
#         break

# n = 32500000
# c = 0
# while True:
#     n += 1
#     ed = find_easy_m(n)
#     if n in ed:
#         ed.remove(n)
#     if len(ed) > 1:
#         s = sum(set(ed))
#         if s % 145 == 0:
#             print(n, s)
#             c += 1
#     if c == 7:
#         break
# c = 0
# n = 23_600_000
# while True:
#     n += 1
#     ed = sorted(set(find_easy_m(n)))
#     if n in ed:
#         ed.remove(n)
#     if len(ed) > 1:
#         m = ed[0] + ed[-1]
#         if m % 213 == 171:
#             print(n, m)
#             c += 1
#     if c == 6:
#         break


# n = 9500000
# c = 0
# while True:
#     n += 1
#     ezd = set(find_easy_m(n))
#     if n in ezd:
#         ezd.remove(n)
#     if len(ezd) > 0:
#         f = sum(ezd) // len(ezd)
#         if f % 813 == 0:
#             print(n, f)
#             c += 1
#     if c == 5:
#         break

# n = 1_475_000
# c = 0
# while n > 0:
#     n -= 1
#     ezd = set(find_easy_m(n))
#     if n in ezd:
#         ezd.remove(n)
#     if len(ezd) > 0:
#         s = sum(ezd)
#         if s <= 42000 and s % 6 == 0:
#             print(n, s)
#             c += 1
#     if c == 5:
#         break


# n = 55_000_000
# c = 0
# while True:
#     n += 1
#     ezd = set(find_easy_m(n))
#     ezd777 = [i for i in ezd if i % 1000 == 777 and i != n]
#     if ezd777:
#         print(n, min(ezd777))
#         c += 1
#     if c == 4:
#         break

# n = 3_333_337
# c = 0
# while True:
#     n += 1
#     ezd = sorted(set(find_easy_m(n)))
#     if n in ezd:
#         ezd.remove(n)
#     if len(ezd) > 1:
#         r = ezd[-1] - ezd[0]
#         if r > 1000 and r % 3 == 0:
#             print(n, r)
#             c += 1
#     if c == 5:
#         break


# c = 0
# for n in range(749_999, 0, -1):
#     ezd = set(find_easy_m(n))
#     ezd7 = [i for i in ezd if i % 10 == 7 and i != n]
#     if len(ezd7) > 0:
#         f = sum(ezd7) // len(ezd7)
#         if f % 111 == 0:
#             print(n, f)
#             c += 1
#     if c == 5:
#         break

# n = 456_789
# c = 0
# while True:
#     n += 1
#     ezd = sorted(set(find_easy_m(n)))
#     if n in ezd:
#         ezd.remove(n)
#     if len(ezd) >= 4:
#         m = ezd[0] + ezd[-1] + ezd[1] + ezd[-2]
#         if m % 114 == 39:
#             print(n, m)
#             c += 1
#     if c == 5:
#         break

# c = 0
# n = 5_400_000
# while True:
#     n += 1
#     ezd = sorted(set(find_easy_m(n)))
#     if n in ezd:
#         ezd.remove(n)
#     if len(ezd) > 1:
#         m = ezd[0] + ezd[-1]
#         if m > 60_000 and str(m) == str(m)[::-1]:
#             print(n, m)
#             c += 1
#     if c == 5:
#         break

# c = 0
# n = 5_700_000
# while True:
#     n += 1
#     ezd = sorted(set(find_easy_m(n)))
#     if n in ezd:
#         ezd.remove(n)
#     if len(ezd) > 1:
#         m = ezd[0] + ezd[-1]
#         if m > 70_000 and int(m**0.5) ** 2 == m:
#             print(n, m)
#             c += 1
#     if c == 5:
#         break

# res = []
# for i in range(125_697, 125_722):
#     ezd = sorted(set(find_easy_m(i)))
#     if len(ezd) == 2 and ezd[0] * ezd[1] == i:
#         res.append([ezd[0] * ezd[1], ezd])

# for i in sorted(res, key=lambda x: x[0]):
#     print(*i[1])


# n = 1324727
# c = 0
# while True:
#     n += 1
#     ezm = find_easy_m(n)
#     if len(ezm) == 2 and all("5" in str(i) for i in ezm):
#         print(n, max(ezm))
#         c += 1
#     if c == 5:
#         break
def find_easy_m(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return [i] + find_easy_m(n // i)
    return [n]


# n = 7_305_678
# c = 0
# while True:
#     n += 1
#     ezm = find_easy_m(n)
#     sezm = sum(ezm)
#     if len(ezm) == 4 and str(sezm) == str(sezm)[::-1]:
#         print(n, sezm)
#         c += 1
#     if c == 5:
#         break

# c = 0
# n = 3502100
# while True:
#     n += 1
#     ezm = find_easy_m(n)
#     if len(ezm) == 4 and any(str(i) == str(i)[::-1] and len(str(i)) == 2 for i in ezm):
#         print(n, max(ezm))
#         c += 1
#     if c == 5:
#         break

# c = 0
# n = 8_000_000


# def multipication(n):
#     m = 1
#     for i in n:
#         m *= i
#     return m


# while True:
#     n += 1
#     ezm = set(find_easy_m(n))
#     if n % 100 == 10 and multipication(ezm) == n:
#         print(n, max(ezm))
#         c += 1
#     if c == 5:
#         break


# n = 5_000_000
# c = 0
# while True:
#     n += 1
#     ezm = sorted(find_easy_m(n))
#     if n % 100 == 12 and any(ezm.count(i) == 5 for i in ezm):
#         print(n, min([i for i in ezm if ezm.count(i) == 5]))
#         c += 1
#     if c == 5:
#         break
# c = 0
# n = 89428304
# while True:
#     n += 1
#     ezm = find_easy_m(n)
#     if len(ezm) >= 6 and n % sum(ezm) == 0:
#         print(n, sum(ezm))
#         c += 1
#     if c == 6:
#         break
# n = 3909600
# c = 0
# while True:
#     n += 1
#     ezm = sorted(find_easy_m(n))
#     if len(ezm) == 7 and max(ezm) > sum(i for i in ezm if i != ezm[-1]):
#         print(n, max(ezm))
#         c += 1
#     if c == 5:
#         break

# c = 0
# n = 123456789
# while True:
#     n += 1
#     ezm = find_easy_m(n)
#     if len(ezm) == 7 and "5" in str(sum(ezm)) and max(ezm) % 10 == 9:
#         print(n, max(ezm))
#         c += 1
#     if c == 5:
#         break

# c = 0
# for i in range(987654320, 0, -1):
#     ezm = find_easy_m(i)
#     if len(ezm) == 13 and "1" in str(sum(ezm)):
#         print(i, max(ezm))
#         c += 1
#     if c == 5:
#         break

# n = 1_000_000
# c = 0
# while True:
#     n += 1
#     for i in range(100):
#         cur = n - 5**i
#         if cur > 0 and cur % 2 == 0 and cur % 111 == 0 and all(int(i) % 2 == 0 for i in str(cur)):
#             print(n, i)
#             c += 1
#             break
#     if c == 5:
#         break
# c = 0
# for i in range(100_000, 1_000_000):
#     if "0" not in str(i):
#         n = 0
#         while i - 3**n > 0:
#             cur = i - 3**n
#             if cur % 2 == 1 and cur % 113 == 0:
#                 print(i, n)
#                 c += 1
#                 break
#             n += 1
#     if c == 5:
#         break
