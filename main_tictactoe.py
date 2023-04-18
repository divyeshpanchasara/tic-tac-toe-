import os


def display_board(board):
    os.system('cls')
    print("{} | {} | {}".format(board[7],board[8],board[9]))
    print("---------")
    print("{} | {} | {}".format(board[4],board[5],board[6]))
    print("---------")
    print("{} | {} | {}".format(board[1],board[2],board[3]))

def update(i,k):
    if board[i]=="X" or board[i]=="O":
        print("the cell is already filled,Re-enter your choice")
        user_input(k)
    else:
        if k==1:
            board[i]=player1
        if k==2:
            board[i]=player2

def user_input(k):
    choice=int(input("Enter player {}'s choice: ".format(k)))
    update(choice,k)

def check_rows():
    if( board[1]==board[2]==board[3]):
        if board[1]==player1:
            return 1
        else:
            return 2
    if( board[4]==board[5]==board[6]):
        if board[4]==player1:
            return 1
        else:
            return 2
    if( board[7]==board[8]==board[9]):
        if board[7]==player1:
            return 1
        else:
            return 2

def check_coloumns():
    if( board[1]==board[4]==board[7]):
        if board[1]==player1:
            return 1
        else:
            return 2
    if( board[2]==board[5]==board[8]):
        if board[2]==player1:
            return 1
        else:
            return 2
    if( board[3]==board[6]==board[9]):
        if board[3]==player1:
            return 1
        else:
            return 2

def check_diagonals():
    if( board[1]==board[5]==board[9]):
        if board[1]==player1:
            return 1
        else:
            return 2
    if( board[3]==board[5]==board[7]):
        if board[3]==player1:
            return 1
        else:
            return 2

def win_or_draw(board):
    
    #this segment checks rows
    if check_rows()==1:
        return 1
    if check_rows()==2:
        return 2
    #this segment checks coloumn
    if check_coloumns()==1:
        return 1
    if check_coloumns()==2:
        return 2
    #this segment checks diagonals
    if check_diagonals()==1:
        return 1
    if check_diagonals()==2:
        return 2
    
    #checks for draw
    count=0
    for i in board[1:]:
        if i=='X' or i=='O':
            count+=1
    if count==9:
        return 0
    

    



board=[0,1,2,3,4,5,6,7,8,9]
os.system('cls')
display_board(board)
player1=input("Choose player1's style X or O: ")
if player1=='X':
    player2='O'
else:
    player1='O'
    player2='X'

game_on=True
p=1
while(game_on):
    if p%2==0:
        p=2
    else:
        p=1
    #takes input of player 1
    user_input(p)
    #displays board
    display_board(board)
    #checks the game condition
    result=win_or_draw(board)
    if result==1:
        print("Player 1 WINS THE GAME!")
        game_on=False
    if result==2:
        print("Player 2 WINS THE GAME!")
        game_on=False
    if result==0:
        print("OPPS! IT'S A DRAW!")
        game_on=False
    p+=1

