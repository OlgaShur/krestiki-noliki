def board():
    print('поле игры')
    print("  0 1 2")
    for i, row in enumerate(board_unit):
        row_str = f"{i} {' '.join(row)}  "
        print(row_str)
    print()
board_unit = [["-"] * 3 for i in range(3) ]
board()

def Hodi():
    while True:
        coordinaty = input("Делайте ваш ход").split()
        if len(coordinaty) != 2:
            print("Введите 2 числа через пробел! ")
            continue
        x, y = coordinaty
        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or  0 > y or  y > 2 :
            print("Координаты вне диапазона! ")
            continue
        if board_unit[x][y] != "-":
            print("Клетка уже занята!")
            continue
        return x, y

def check_win():
    win_cordinaty = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cordinaty:
        memo = []
        for c in cord:
            memo.append(board_unit[c[0]][c[1]])
        if memo == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if memo == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

print('Игра "Крестики-Нолики"!')
print("формат ввода: x y ")
print("x - номер строки  ")
print("y - номер столбца ")
print('Начинаем!')

nomer_hoda = 0
while True:
    nomer_hoda += 1
    board()
    if nomer_hoda % 2 == 1:
        print("Ходит X!")
    else:
        print("Ходит 0!")

    x, y = Hodi()

    if nomer_hoda % 2 == 1:
        board_unit[x][y] = "X"
    else:
        board_unit[x][y] = "0"

    if check_win():
        break

    if nomer_hoda == 9:
        print("Ничья!")
        break

