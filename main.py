def f(x, y):
    return int(x and y)
def f1(x,y):
    return int(x or y)
def f2(x,y):
    return int(x <= y)
def f3(x,y):
    return int(x == y)
def f4(x,y):
    return int(not(x and y))
def f5(x,y):
    return int(not(x) or not(y))
def f6(x,y,w):
    return int((not(not(x and y)) or w))
def f7(x,y,w):
    return int(x and y or w)
print('конъюнкция')
print("+---+---+--------+")
print("| x | y | f(x,y) |")
print("+---+---+--------+")
for x in range(2):
    for y in range(2):
        print("|", x, "|", y, "|", f(x,y), "     |")
print("+---+---+--------+")
print("\n")
print('дизъюнкция')
print("+---+---+--------+")
print("| x | y | f(x,y) |")
print("+---+---+--------+")
for x in range(2):
    for y in range(2):
        print("|", x, "|", y, "|", f1(x,y), "     |")
print("+---+---+--------+")
print("\n")
print('импликация')
print("+---+---+--------+")
print("| x | y | f(x,y) |")
print("+---+---+--------+")
for x in range(2):
    for y in range(2):
        print("|", x, "|", y, "|", f2(x,y), "     |")
print("+---+---+--------+")
print("\n")
print('экваваленция')
print("+---+---+--------+")
print("| x | y | f(x,y) |")
print("+---+---+--------+")
for x in range(2):
    for y in range(2):
        print("|", x, "|", y, "|", f3(x,y), "     |")
print("+---+---+--------+")
print("\n")
print('Закон де Моргана')
print("+---+---+--------+--------+")
print("| x | y | f(x,y) | g(x,y) |")
print("+---+---+--------+--------+")
for x in range(2):
    for y in range(2):
        print("|", x, "|", y, "|", f4(x,y), "     |", f5(x,y), "     |")
print("+---+---+--------+--------+")
print("\n")
print('зависимость с 3мя переменными')
print("+---+---+---+--------+--------+")
print("| x | y | w | f(x,y) | g(x,y) |")
print("+---+---+---+--------+--------+")
for x in range(2):
    for y in range(2):
        for w in range(2):
            print("|", x, "|", y, "|", w, "|", f6(x,y,w), "     |", f7(x,y,w), "     |")
print("+---+---+---+--------+--------+")




