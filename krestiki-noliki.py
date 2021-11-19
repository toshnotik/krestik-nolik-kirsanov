
print("-Крестики нолики-")

board = [["-"] * 3 for _ in range(3)]
steps = 0


def show_board(f):
    print('  0 1 2')
    for i in range(len(board)):
        print(str(i), *board[i])


def user_input(f):
    while True:
        step = input('Введите координаты хода: ').split()
        if len(step) != 2:
            print('Введите две координаты')
            continue

        if not(step[0].isdigit() and step[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, step)

        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Вышли из диапозона поля')
            continue
        if f[x][y] != '-':
            print('Поле занято')
            continue
        break
    return x, y


def wins(f, user):
    win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
           ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
           ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win:
        symbol = []
        for i in cord:
            symbol.append(f[i[0]][i[1]])
        if symbol == [user, user, user]:
            return True
    return False


while True:
    if steps == 9:
        print('Ничья')
        break
    if steps % 2 == 0:
        user = 'X'
    else:
        user = 'O'
    show_board(board)
    x, y = user_input(board)
    board[x][y] = user
    if wins(board, user):
        print(f'Выйграл {user}')
        show_board(board)
        break
    steps += 1


