

board = [[1,1,1], [1,1,1], [1,1,1 ]]
print board[0]
print board[1]
print board[2]

while True:
    mark1 = raw_input("enter 0 or X: ")
    r = int(raw_input("now enter row: "))
    c = int(raw_input("now enter col: "))
    board[r][c] = mark1
    print board[0]
    print board[1]
    print board[2]
    if board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':
        print 'player with 0 won the game'
        break
    if board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
        print 'player with 0 won the game'
        break
    if board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0':
        print 'player with 0 won the game'
        break
    if board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':
        print 'player with 0 won the game'
        break
    if board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0':
        print 'player with 0 won the game'
        break
    if board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
        print 'player with 0 won the game'
        break
    if board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0':
        print 'player with 0 won the game'
        break
    if board[2][0] == '0' and board[1][1] == '0' and board[0][2] == '0':
        print 'player with 0 won the game'
        break
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print 'player with X won the game'
        break
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        print 'player with X won the game'
        break
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print 'player with X won the game'
        break
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print 'player with X won the game'
        break
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        print 'player with X won the game'
        break
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print 'player with X won the game'
        break
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        print 'player with X won the game'
        break
    if board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
        print 'player with X won the game'
        break
