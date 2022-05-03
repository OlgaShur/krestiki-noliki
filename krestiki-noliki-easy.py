def pole():
    print('поле игры')
    print('_ _ _')
    print(board_start[0],board_start[1],board_start[2])
    print(board_start[3],board_start[4],board_start[5])
    print(board_start[6],board_start[7],board_start[8])
    print('_ _ _')


board_start = list(range(1,10))
pole()
print('Приветствую в игре "Крестики-Нолики". Решите, кто будет ходить первым?\nПервый будет играть крестиками - Х.')

# функция, определяющая победные комбинации
def winner(W):
    win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)) #победные комбинации
    for i in range(0,8): #если случилась победная комбинация - присвоить переменной W значение победы
        if board_start[win[i][0]] == board_start[win[i][1]] == board_start[win[i][2]] == sign:
            W = 'Ура! Победа! Вы выиграли!'
            return W
    return 'Играем дальше'

W = 'Играем дальше'
nomer_hoda = 1

#Цикл игры - пока номер хода меньше 9 и победитель не определен:
while nomer_hoda <= 9 and W == 'Играем дальше': #цикл работает пока номер хода <10 и переменная W - "равна играем дальше"
    if nomer_hoda%2 == 0: # если номер хода кратен 2 - играют Нули
        sign = 'O' # присвоили переменной значение Нуля
        mesto = input('Куда поставить О?(выберите незанятое поле (целое число) от 1 до 9): ') # спросили, куда ставить ход
        if not(mesto.isdigit()):
            print("Введите целое число! ")
            continue
        mesto = int(mesto)
        if (1 <= mesto <= 9) and mesto in board_start:  # если ход  в рамках поля и место свободно
            board_start[mesto-1] = sign # присваиваем месту в поле значение Нуля
        else: # если нет - выдать ошибку
            print('Место не существует или занято. Выбери другое место!')
    else:  # если номер хода не кратен 2 - играют Иксы и далее все то же самое для Икса
        sign = 'X'
        mesto = input('Куда поставить X?(выберите незанятое поле (целое число) от 1 до 9): ')
        if not(mesto.isdigit()):
            print("Введите целое число! ")
            continue
        mesto = int(mesto)
        if (1 <= mesto <= 9) and mesto in board_start:
            board_start[mesto-1] = sign
        else:
            print('Место не существует или занято. Выбери другое место!')
    W = winner(W) #  присваиваем переменной W значение функции winner
    if nomer_hoda == 9 and W == 'Играем дальше': # если номер хода равен 9 и еще никто не выиграл - ничья.
        print('Вы сыграли в ничью')
    else:
        print(W)
    nomer_hoda += 1
    pole()
