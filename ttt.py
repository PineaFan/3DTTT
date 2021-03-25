import os
global pCols, board


class c:
    c = '\033[0m'
    White = '\033[1m'
    Italics = '\033[3m'
    Underline = '\033[4m'
    BlinkItalics = '\033[5m'
    BlinkInverted = '\033[7m'
    Strike = '\033[28m'
    Invisible = '\033[30m'
    RedDark = '\033[31m'
    GreenDark = '\033[32m'
    YellowDark = '\033[33m'
    BlueDark = '\033[34m'
    PinkDark = '\033[35m'
    CyanDark = '\033[36m'
    RedDarkInverted = '\033[41m'
    GreenDarkInverted = '\033[42m'
    YellowDarkInverted = '\033[43m'
    BlueDarkInverted = '\033[44m'
    PinkDarkInverted = '\033[45m'
    CyanDarkInverted = '\033[46m'
    WhiteDarkInverted = '\033[47m'
    Grey = '\033[90m'
    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Pink = '\033[95m'
    Cyan = '\033[96m'
    RedInverted = '\033[101m'
    GreenInverted = '\033[102m'
    YellowInverted = '\033[103m'
    BlueInverted = '\033[104m'
    PinkInverted = '\033[105m'
    CyanInverted = '\033[106m'
    WhiteInverted = '\033[107m'


pCols = [c.Red, c.Cyan, c.Green, c.Yellow]


class Player:
    def __init__(self, prefix, name):
        self.points = 0
        self.prefix = prefix
        self.name = name[:8] + (" "*(8-len(name[:8])))


def clearBoard():
    global board
    board = [
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ],
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    ]


def printBoard(players, turn, text, p, game):
    global pCols, board
    try:
        tw, th = os.popen('stty size', 'r').read().split()
        term = [int(tw), int(th)]
    except Exception as e:
        print(e)
        term = [int(272), int(68)]
    for x in range(0, term[0]-15):
        print()
    print(f'{c.c}{"-"*65}')
    print(f'{c.c}|{" "*((len(board)*2) + 1)}| {c.White}3D Tic Tac Toe{c.c} - Round {game}{" "*(19-len(str(game)))}|')
    print(f'|{" "*9}{c.Red}{p[board[0][0][0]]} {p[board[0][0][1]]} {p[board[0][0][2]]}{c.c}     |{" "*18}{c.White}Scores{c.c}{" "*19}|')
    print(f'|{" "*8}{c.Green}{p[board[0][1][0]]} {p[board[0][1][1]]} {p[board[0][1][2]]}{c.c}      |{"-"*43}|')
    print(
        f'|{" "*7}{c.Pink}{p[board[0][2][0]]} {p[board[0][2][1]]} {p[board[0][2][2]]}{c.c}       |   P1 {players[0].prefix if len(players)>0 else " "}  '
        f' |   P2 {players[1].prefix if len(players)>1 else " "}   |   P3 {players[2].prefix if len(players)>2 else " "}   |   '
        f'P4 {players[3].prefix if len(players)>3 else " "}   |'
    )
    print(
        f'|{" "*19}{c.c}| {pCols[0]}{players[0].name if len(players)>0 else " "*8}{c.c} | '
        f'{pCols[1]}{players[1].name if len(players)>1 else " "*8}{c.c} | {pCols[2]}{players[2].name if len(players)>2 else " "*8}{c.c} '
        f'| {pCols[3]}{players[3].name if len(players)>3 else " "*8} {c.c}|'
    )
    print(f'|{" "*9}{c.Red}{p[board[1][0][0]]} {p[board[1][0][1]]} {p[board[1][0][2]]}{c.c}     |{"-"*43}|')
    print(
        f'|{" "*8}{c.Green}{p[board[1][1][0]]} {p[board[1][1][1]]} {p[board[1][1][2]]}{c.c}      | '
        f'{(str(players[0].points) + (" Win " if players[0].points == 1 else " Wins") + " "*(3-len(str(players[0].points)))) if len(players)>0 else " "*8} '
        f'| {(str(players[1].points) + (" Win " if players[1].points == 1 else " Wins") + " "*(3-len(str(players[1].points)))) if len(players)>1 else " "*8} '
        f'| {(str(players[2].points) + (" Win " if players[2].points == 2 else " Wins") + " "*(3-len(str(players[2].points)))) if len(players)>2 else " "*8} '
        f'| {(str(players[3].points) + (" Win " if players[3].points == 1 else " Wins") + " "*(3-len(str(players[3].points)))) if len(players)>3 else " "*8} |'
    )
    print(f'|{" "*7}{c.Pink}{p[board[1][2][0]]} {p[board[1][2][1]]} {p[board[1][2][2]]}{c.c}       |{"-"*43}|')
    print(f'|{" "*19}|{" "*43}|')
    print(
        f'|{" "*9}{c.Red}{p[board[2][0][0]]} {p[board[2][0][1]]} {p[board[2][0][2]]}{c.c}     |  ' +
        (f'It is {pCols[turn]}Player {turn+1}\'s ({players[turn].name}){c.c} turn.        |' if text > -1 else (' '*41 + '|'))
    )
    print(
        f'|{" "*8}{c.Green}{p[board[2][1][0]]} {p[board[2][1][1]]} {p[board[2][1][2]]}{c.c}      |  ' +
        (f'Type either {c.Green}1 2{c.c} or {c.Green}3{c.c} to select {"top, " if text==0 else "left," if text==1 else "back,"}     |' if text > -1 else (' '*41 + '|'))
    )
    print(
        f'|{" "*7}{c.Pink}{p[board[2][2][0]]} {p[board[2][2][1]]} {p[board[2][2][2]]}{c.c}       |  ' +
        (f'middle or {"bottom." if text==0 else "right. " if text==1 else "front. "}{" "*24}|' if text > -1 else (' '*41 + '|'))
    )
    print(f'|{" "*19}|{" "*43}|')
    print(f'{c.c}{"-"*65}')


def checkForWin():
    for x in board:  # For each layer
        for row in x:
            if row[0] == row[1] == row[2] and row[0] > 0:
                return row[0]  # Rows
        for y in range(0, len(x)):  # For each list
            if x[0][y] == x[1][y] == x[2][y] and x[0][y] > 0:
                return x[0][y]  # Columns
        if ((x[0][0] == x[1][1] == x[2][2]) or (x[0][2] == x[1][1] == x[2][0])) and x[1][1] > 0:
            return x[1][1]  # Diagonals

    for x in range(0, len(board)):  # For each vertical plane
        for y in range(0, len(board)):  # For each vertical column
            if board[0][x][y] == board[1][x][y] == board[2][x][y] and board[0][x][y] > 0:
                return board[0][x][y]  # Vertical line
        if ((board[0][x][0] == board[1][x][1] == board[2][x][2]) or (board[0][x][2] == board[1][x][1] == board[2][x][0])) and board[1][x][1] > 0:
            return board[1][x][1]  # Vertical diagonals

    for x in range(0, len(board)):  # For each vertical column
        if ((board[0][0][x] == board[1][1][x] == board[2][2][x]) or (board[0][2][x] == board[1][1][x] == board[2][0][x])) and board[1][1][x] > 0:
            return board[1][1][x]  # Back diagonals

    if (
        (board[0][0][0] == board[1][1][1] == board[2][2][2]) or
        (board[0][0][2] == board[1][1][1] == board[2][2][0]) or
        (board[0][2][0] == board[1][1][1] == board[2][0][2]) or
        (board[0][2][2] == board[1][1][1] == board[2][0][0])
    ) and board[1][1][1] > 0:
        return board[1][1][1]  # Full diagonals


def gameLoop():
    game = 0
    players = []
    prefixes = {0: '`'}
    print(c.White + "3D Tic Tac Toe")
    print()
    print(f'{c.c}Each player needs a 1 character {c.Green}prefix{c.c} to show their square on the board,')
    print(f'and a {c.Green}name{c.c} for the scoreboard.')
    print(f'Leave the {c.Green}prefix{c.c} field blank to stop adding players.')
    print('\nPress enter to continue')
    input(f'{c.Green}setup{c.c}@3Dttt {c.Green}~/Continue{c.c}> {c.Invisible}')
    for x in range(0, 4):
        prefix = input(f'{c.Green}setup{c.c}@3Dttt {c.Green}~/Player{x+1}/Prefix{c.c}> {c.Cyan}')
        if prefix != '':
            name = ''
            while name == '':
                name = input(f'{c.Green}setup{c.c}@3Dttt {c.Green}~/Player{x+1}/Name{c.c}> {c.Cyan}')
                if name == '':
                    print(f'{c.Red}Please enter a valid name')
            print(c.c + "Player added")
        else:
            break
        players.append(Player(prefix[:1], name))
        prefixes[len(prefixes)] = prefix
    while True:
        clearBoard()
        game += 1
        won = False
        while won is False:
            for x in range(0, len(players)):
                moveAllowed = False
                error = ''
                while True:
                    moveCoords = [-1, -1, -1]
                    for y in range(0, 3):
                        printBoard(players, x, y, prefixes, game)
                        print(error)
                        while True:
                            moveCoords[y] = input(f'{c.Green}Player{x+1}{c.c}@3Dttt {c.Green}~/Move{c.c}> {pCols[x]}')
                            try:
                                moveCoords[y] = int(moveCoords[y])
                            except (IndexError, ValueError):
                                moveCoords[y] = 0
                            if (0 < moveCoords[y] < 4):
                                break
                            printBoard(players, x, y, prefixes, game)
                            print(c.RedDark + "Please pick a value from 1 to 3")
                    moveAllowed = not board[moveCoords[0]-1][moveCoords[2]-1][moveCoords[1]-1]
                    if moveAllowed:
                        board[moveCoords[0]-1][moveCoords[2]-1][moveCoords[1]-1] = x+1
                        break
                    else:
                        error = c.RedDark + "That space is taken, please select another."
                winner = checkForWin()
                if winner:
                    won = True
                    break
        players[winner-1].points += 1
        printBoard(players, 0, -1, prefixes, game)
        print(pCols[winner-1] + 'Player ' + str(winner) + ' won | Press enter to continue...')
        input(f'{c.Green}setup{c.c}@3Dttt {c.Green}~/Continue{c.c}> {c.Invisible}')


gameLoop()
