player = "A"

board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]

def print_board(board):
    print("\t13\t12\t11\t10\t9\t8")
    print("---------------------------------------------------------")
    print("B:\t" + str(board[13]) + "\t" + str(board[12]) + "\t" + str(board[11]) + "\t" + str(board[10]) + "\t" + str(board[9]) + "\t" + str(board[8]))
    print("   " + str(board[0]) + "                                                   " + str(board[7]))
    print("A:\t" + str(board[1]) + "\t" + str(board[2]) + "\t" + str(board[3]) + "\t" + str(board[4]) + "\t" + str(board[5]) + "\t" + str(board[6]))
    print("---------------------------------------------------------")
    print("\t1\t2\t3\t4\t5\t6")

def is_valid_move(pocket):
    if board[pocket] == 0:
        return False
    else:
        if player == "A":
            if pocket == 1 or pocket == 2 or pocket == 3 or pocket == 4 or pocket == 5 or pocket == 6:
                return True
            else:
                return False
        else:
            if pocket == 8 or pocket == 9 or pocket == 10 or pocket == 11 or pocket == 12 or pocket == 13:
                return True
            else:
                return False

def move_stones(pocket):
    stones = board[pocket]
    board[pocket] = 0
    
    #This loop moves the stones
    while stones > 0:
        if player == "B" and pocket == 6:
            pocket = 7
        elif player == "A" and pocket == 13:
            pocket = 0
        elif pocket == 13:
            pocket = -1    
       
        board[pocket+1] += 1
        pocket+=1
        stones -=1

    #This if statement checks if the spot you landed on has no stones
    if player == "A" and (pocket == 1 or pocket == 2 or pocket == 3 or pocket == 4 or pocket == 5 or pocket == 6):
        if board[pocket] == 1:
            board[7] = board[7] + board[pocket] + board[14 - pocket]
            board[pocket] = 0
            board[14 - pocket] = 0
    elif player == "B" and (pocket == 8 or pocket == 9 or pocket == 10 or pocket == 11 or pocket == 12 or pocket == 13):
        if board[pocket] == 1:
            board[0] = board[0] + board[pocket] + board[14 - pocket]
            board[pocket] = 0
            board[14 - pocket] = 0
            
    print_board(board)
    
    game_over()
    if game_over() == True:
        return
    
    #This if statement gives you another turn if you land in your goal
    if player == "A" and pocket == 7:
        print("Go again!")
        take_turn()
    elif player == "B" and pocket == 0:
        print("Go again!")
        take_turn()
        
   
   
        
def take_turn():
    print("Player " + player + "'s turn!")
    if player == "A":
        print("Possible moves: 1, 2, 3, 4, 5, 6")
    else:
        print("Possible moves: 8, 9, 10, 11, 12, 13")
    
    pocket = int(input("Choose a pocket: ")) 
    is_valid_move(pocket)
    
    while is_valid_move(pocket) == False:
        print("Please enter a valid move.")
        pocket = int(input("Choose a pocket: ")) 
        is_valid_move(pocket)
    
    move_stones(pocket)
        
  
def game_over():
    if (board[1] == 0 and board[2] == 0 and board[3] == 0 and board[4] == 0 and board[5] == 0 and board[6] == 0) or (board[8] == 0 and board[9] == 0 and board[10] == 0 and board[11] == 0 and board[12] == 0 and board[13] == 0):
        return True
    else:
        return False
        
def calculate_winner(board):
    if (board[1] == 0 and board[2] == 0 and board[3] == 0 and board[4] == 0 and board[5] == 0 and board[6] == 0):
        board[0] = board[0] + board[8] + board[9] + board[10] + board[11] + board[12] + board[13]
    else:
        board[7] = board[7] + board[1] + board[2] + board[3] + board[4] + board[5] + board[6]
        
    print("Player A score: " + str(board[7]))
    print("Player B score: " + str(board[0]))
        
    if board[0] > board[7]:
        print("Player B is the winner!")
    elif board[7] > board[0]:
        print("Player A is the winner!")
    else:
        print("The game is a tie!")
        


print_board(board)
take_turn()

while game_over() == False:
    if player == "A":
        player = "B"
    else:
        player = "A"
    take_turn()    


        
print("Game over")
calculate_winner(board)
