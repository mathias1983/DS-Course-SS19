board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
player = "X"

def draw_bord():
    i = 0
    while i < 9:
        print(board[i], board[i+1], board[i+2])
        i += 3
    else:
        print()

def choose_move():
    while True:
        number = input()
        if number.isdigit() == False:
            print("\nPlease enter a valid number")
            continue

        number = int(number)

        if number >= 0 and number < 9 :
            if is_valid_move(number):
                return number
            else:
                print("\nThis move has already been made")
        else:
            print("\nPlease enter a number from 1 to 9")


def change_player(player):
    if player == "X":
        return "O"
    return "X"

def is_valid_move(number):
    return board[number].isdigit()

def unused_move_left():
    for i in board:
        if i.isdigit():
            return True
    return False

def is_game_won():
    return is_streak_vertical() or is_streak_horizontal() or is_streak_diagonal_left() or is_streak_diagonal_right()



def is_streak_vertical():
    for i in range(3):
        count = 0
        for j in range(3):
            pos = i + (j * 3)
            if board[pos] == player:
                count += 1
            if count == 3:
                return True

    return False



def is_streak_horizontal():
    for i in range(3):
        count = 0
        for j in range(3):
            pos = (i * 3) + j
            if board[pos] == player:
                count += 1
            if count == 3:
                return True

    return False

def is_streak_diagonal_left():
    return board[0] == player and board[4] == player and board[8] == player

def is_streak_diagonal_right():
    return board[2] == player and board[4] == player and board[6] == player


while True:
    draw_bord()
    if unused_move_left() == False:
        print("There are no more moves left. Tie!")
        break

    print("Player %s please choose a number" % player)
    board[choose_move()] = player
    print()

    if is_game_won():
        draw_bord()
        print("Player %s wins!" % player)
        break

    player = change_player(player)

