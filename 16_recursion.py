# 1 лёгкая
# def F(n):
#     if n < 3: return 1
#     if n % 2 == 0: return F(n - 1) + n - 1
#     return F(n - 2) + 2* n - 2
#
# print(F(8))

# 2 убираем лимит до 1000
# from sys import setrecursionlimit
#
# def F(n):
#     if n<3: return 3
#     return 2*n + 5 + F(n-2)
#
# setrecursionlimit(1600)
# print(F(3027) - F(3023))

# 3 кэш
# from functools import lru_cache
#
# @lru_cache(None)
# def F(n):
#     if n<7: return 7
#     return n+1+F(n-2)
#
# for i in range(0, 2025):
#     F(i)
#
# print(F(2024) - F(2022))

# сложное
# from functools import lru_cache
#
# @lru_cache(None)
# def G(n):
#     if n<10: return 2 * n
#     if n >= 10: return G(n-2) + 1
#
# @lru_cache(None)
# def F(n):
#     return 2 * (G(n-3) + 8)
#
# for i in range(0, 15548):
#     F(i)
#
# print(F(15548))

from functools import lru_cache


def F(n):
    if n >= 19: return F(n-4) + 3580
    return 6 * (G(n-7) - 36)

@lru_cache(None)
def G(n):
    if n >= 248045: return n/20 + 28
    return G(n+9) - 4

for i in range(250000, 0, -1):
    G(i)

print(F(673))