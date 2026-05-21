# если одна куча => x
# если две => x, y
# если три => x, y, z
# s - сколько ходов осталось до конца игры

def f(x, s):
    # победил всегда походил и оставил четное число, если true значит победил, тот кто должен
    if x >= 40: return s % 2 == 0
    # если ходы закончились и никто не победил
    if s == 0: return False
    # варианты всех ходов
    h = [f(x+1, s-1), f(x+4, s-1), f(x*2, s-1)]

    if (s-1) %2 == 0: return any(h)
    else: return all(h)

print("19)")
for x in range(1, 40):
    if f(x,2):
        print(x)

# запретили побеждать первым ходом
print("20)")
for x in range(1, 40):
    if f(x,3) and not f(x, 1):
        print(x)

print("21) ")
for x in range(1, 40):
    if f(x,4) and not f(x, 2):
        print(x)


# 2 кучи или больше, 19 (если противник лошара)
# any - у противника рассматриваем все случаи
def f(x, y, s):
    if x + y >= 259: return s % 2 == 0
    if s == 0: return False
    h = [f(x+1, y, s-1), f(x*2, y, s-1), f(x, y+1, s-1), f(x, y*2, s-1)]
    if (s-1) %2 == 0: return any(h)
    else: return any(h)

print("19)")
for x in range(1, 242):
    if f(x,17, 2):
        print(x)

# 2 кучи или больше 20-21
def f(x, y, s):
    if x + y >= 259: return s % 2 == 0
    if s == 0: return False
    h = [f(x+1, y, s-1), f(x*2, y, s-1), f(x, y+1, s-1), f(x, y*2, s-1)]
    if (s-1) %2 == 0: return any(h)
    else: return all(h)

print("20)")
for x in range(1, 242):
    if f(x,17, 3) and not f(x, 17, 1):
        print(x)

print("21)")
for x in range(1, 242):
    if f(x,17, 4) and not f(x, 17, 2):
        print(x)