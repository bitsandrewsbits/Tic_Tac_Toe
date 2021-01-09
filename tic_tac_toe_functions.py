def show_table(pole):
    print(pole[0], pole[1], pole[2])
    print(pole[3], pole[4], pole[5])
    print(pole[6], pole[7], pole[8])

def check_winner(pole,winner):
    if pole[1] != '1':
        if pole[1] == pole[2] == pole[3]:
            winner = pole[1]
        elif pole[1] == pole[4] == pole[7]:
            winner = pole[1]
        elif pole[1] == pole[5] == pole[9]:
            winner = pole[1]
    if pole[2] != '2':
        if pole[2] == pole[5] == pole[8]:
            winner = pole[2]
    if pole[3] != '3':
        if pole[3] == pole[5] == pole[7]:
            winner = pole[3]
        elif pole[3] == pole[6] == pole[9]:
            winner = pole[3]
    if pole[4] != '4':
        if pole[4] == pole[5] == pole[6]:
            winner = pole[4]
    if pole[7] != '7':
        if pole[7] == pole[8] == pole[9]:
            winner = pole[7]
    return winner

def take_step(turn):
    if turn == 'O':
        return 'X'
    else:
        return 'O'

def random_pole_bot(pole, pole_bot, turn):
    import random
    flag1 = True
    while flag1:
        choice = str(random.choice(pole_bot))
        for i in range(len(pole)):
            if choice == pole[i]:
                pole_bot.remove(pole[i])
                pole[i] = turn
                flag1 = False
