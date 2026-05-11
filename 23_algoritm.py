def f(start,end):
    if start == end: return 1
    if start < end: return 0
    return f(start-1, end) + f(start - 3, end) + f(start // 3, end)

print(f(22, 2))


def f(start,end):
    if start == end: return 1
    if start < end: return 0
    return f(start-2, end) + f(start // 2, end)

print(f(28, 10) *  f(10, 1))


def f(start,end):
    if start == end: return 1
    if start < end or start == 16 or start == 9: return 0
    return f(start-1, end) + f(start-2, end) + f(start // 3, end)

print(f(19, 3))