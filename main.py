# Assignment: Tic Tac Toe
# Build a text-based version of the Tic Tac Toe game.
"""
Using what you have learnt about Python programming, you will build a text-based version of the Tic Tac Toe game.
The game should be playable in the command line just like the Blackjack game we created on Day 11.
It should be a 2-player game, where one person is "X" and the other plays "O".

This is a simple demonstration of how the game works:
https://www.google.com/search?q=tic+tac+toe


You can choose how you want your game to look.
The simplest is to create a game board using "|" and "_" symbols.
But the design is up to you.
...

If you have more time, you can challenge yourself to build an AI player to play the game with you.
"""

# Approach/ Steps to take
"""
1.Create TicTacToe board (with coordinates so that players can know what value to input for which location)
2.Let different players take turns (same player can only place similar symbols) to choose where to place their token 
 Ask for player input
    -- How to take note of whose turn is it?
    -- Update board to display new game state ---How to use f string in multiline comment? Or display list in multilines??
    -- Don't allow symbols to be placed on same/occupied spot 
    -- Don't want to keep printing 9 images for each player input in algorithm.
       How to account for board state without keep printing new image? Instead just want to add an X or O in original board
       Keep track of board state through list- index 0 to 8; 0 = top left, 2 = top right, 8 = bottom right
       Use key value pairs for coordinates to update list (eg. "A1":0 etc...)

3.Check for win condition; 3 similar symbols in a row 
    -- Dont allow for another player to place token if already win; how to break/skip certain parts of loop? (just break loop; win statement displayed outside of loop)
4.Check for draw condition

Some issues- 
Better define coordinate system- [XY] which is x and which is y; should have flipped x & y values
Cant convert string to tuple

#Fix the important stuff first #Function over form 
Minor improvements- not crucial for program function; just for nicer display/neater 
-Clear console (python clear console before print); 
-Add borders | and square boundaries ----, strip string quotation marks 

References used:
>>tic tac toe win condition
>>print list in multiple lines python
>>how to convert string to tuple[]/value python (for dictionary [][])
>>how to convert string to character
>>type casting
>>print list elements in new line
>>how to keep asking for user input python until valid
"""

"""from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')"""

import numpy as np

# Tic-Tac-Toe Board: 3 lists representing each row instead of 1 single list with 9 items
board_state = [["|_|", "|_|", "|_|"],
               ["|_|", "|_|", "|_|"],
               ["|_|", "|_|", "|_|"]
               ]
# board_state_display = ('\n'.join(str(x) for x in board_state))
# values doesnt update automatically unless called

# Test change board_state
# board_state[0][0] = "X"
# board_state[0][1] = "Y"
# board_state[0][2] = "Z"
# board_state[1][0] = "A"
# board_state[1][1] = "B"
# board_state[1][2] = "C"
# board_state[2][0] = "D"
# board_state[2][1] = "E"
# board_state[2][2] = "F"

# How to convert string/dictionary value into tuple object?
# how to convert string to character python
# how to convert string to [] item python
# python type casting

# coordinate = {"A1": "[0][0]",
#               "B1": "[0][1]",
#               "C1": "[0][2]",
#               "A2": "[1][0]",
#               "B2": "[1][1]",
#               "C2": "[1][2]",
#               "A3": "[2][0]",
#               "B3": "[2][1]",
#               "C3": "[2][2]", }
# print(board_state[coordinate["A1"]])
# print(board_state[0][0])

# Workaround; no choice cant use [0][0] directly from dictionary
coordinate = {"A1": "0 0",
              "B1": "0 1",
              "C1": "0 2",
              "A2": "1 0",
              "B2": "1 1",
              "C2": "1 2",
              "A3": "2 0",
              "B3": "2 1",
              "C3": "2 2", }


# Deciphers player input & changes to coordinate in order to determine symbol to be placed at particular location
def coordinate_input(xy):
    global x_cor
    global y_cor
    coordinate_indexes = (coordinate[xy].split())
    # print(coordinate_indexes)
    for i in range(1):
        x_cor = int(coordinate_indexes[i])
        y_cor = int(coordinate_indexes[i + 1])


# Displays board_state
def update_board():
    board_state_display = ('\n'.join(str(x) for x in board_state))
    print(board_state_display)


# Check for draw state
# If board all filled and no winner; draw--- check after player 1 bcos theres 9 slots; 2 players = 4 turns + 1 more turn for p1
# Only return board_totally_filled aft all rows checked
# But if fill last row first; then will trigger true
# Can't check individually bcos 1 non "_" symbol will proc filled condition. Problem only arises aft u changed to 3 lists; cant use (not in)
# Workaround - Use reference list to verify if board is filled
def is_board_filled():
    global board_totally_filled
    is_square_filled = []
    for i in range(len(board_state)):
        for j in range(len(board_state[i])):
            if "|_|" not in board_state[i][j]:
                is_square_filled.append(1)
            else:
                is_square_filled.append(0)
    print(is_square_filled)
    if 0 not in is_square_filled:
        board_totally_filled = True
        print("BOARD TOTALLY FILLED!!!")


# WIN CONDITION- CHECK AFT EACH PLAYER -- IMPLEMENT FUNCTION FOR FUNCTION CALL??
# Any easier way to check for win con? Feels a little repetitive
# NEW IDEA: USE LIST TO CHECK FOR WIN CONDITION?; Assign 1 or 2 to list indexes and if fulfill 3 in a row condition, win
#           But also feels repetitive... And doesnt work; no coordinate to reference to; has coordinate aft adding 1,2 & 0
"""
How to check for 3 in a row?
straight 012,345,678,036,147,258
diagonal 048,642
   A B C            
1 |00|01|02|            |0|1|2|
2 |10|11|12|            |3|4|5|
3 |20|21|22|            |6|7|8|
"""

# Checking wins- all scenarios --- Win condition bug; will proc win if all blanks -- dont set win variable in check but with conditions in main loop
def tic_tac_win(tttboard):
    global tick_win
    #Check for rows and columns
    for board in [np.transpose(tttboard), tttboard]:
        winning_board = check_win_rows(board)
        if winning_board:
            # tick_win = True
            # print(winning_board)
            return winning_board
    #Then diagonals
    return check_wins_diagonals(tttboard)

# Checking rows
# If all same items in the row; will return length of 1 (bcos of python set properties)
def check_win_rows(tttboard):
    for row in tttboard:
        if len(set(row)) == 1:
            # print(row[0])
            return row[0]
    return 0

# Checking diagonals
def check_wins_diagonals(tttboard):
    global tick_win
    #Check for [1][1], [2][2] & [3][3]. len(tttboard) =3
    if len(set([tttboard[i][i] for i in range(len(tttboard))])) == 1:
        # tick_win=True
        # print(tttboard[0][0])
        return tttboard[0][0]
    return 0

# def tic_tac_win():
#     global tick_win
#     global winner
#
#     # ACCOUNTING FOR ALL WIN CON: TEDIOUS BUT PROVEN WAY
#     if board_state[0][0] == "|X|" and board_state[0][1] == "|X|" and board_state[0][2] == "|X|":
#         # if (board_state[0][0]] and board_state[0][1]] and board_state[0][2])== "X":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 012")
#     elif board_state[1][0] == "|X|" and board_state[1][1] == "|X|" and board_state[1][2] == "|X|":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 345")
#     elif board_state[2][0] == "|X|" and board_state[2][1] == "|X|" and board_state[2][2] == "|X|":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 678")
#     elif board_state[0][0] == "|X|" and board_state[1][0] == "|X|" and board_state[2][0] == "|X|":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 036")
#     elif board_state[0][1] == "|X|" and board_state[1][1] == "|X|" and board_state[2][1] == "|X|":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 147")
#     elif board_state[0][2] == "|X|" and board_state[1][2] == "|X|" and board_state[2][2] == "|X|":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 258")
#     elif board_state[0][0] == "|X|" and board_state[1][1] == "|X|" and board_state[2][2] == "|X|":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 0][0]48")
#     elif board_state[2][0] == "|X|" and board_state[1][1] == "|X|" and board_state[0][2] == "|X|":
#         tick_win = True
#         winner = "Player 1"
#         print("P1W 642")
#
#     if board_state[0][0] == "|O|" and board_state[0][1] == "|O|" and board_state[0][2] == "|O|":
#         tick_win = True
#         winner = "Player 2"
#     elif board_state[1][0] == "|O|" and board_state[1][1] == "|O|" and board_state[1][2] == "|O|":
#         tick_win = True
#         winner = "Player 2"
#     elif board_state[2][0] == "|O|" and board_state[2][1] == "|O|" and board_state[2][2] == "|O|":
#         tick_win = True
#         winner = "Player 2"
#     elif board_state[0][0] == "|O|" and board_state[1][0] == "|O|" and board_state[2][0] == "|O|":
#         tick_win = True
#         winner = "Player 2"
#     elif board_state[0][1] == "|O|" and board_state[1][1] == "|O|" and board_state[2][1] == "|O|":
#         tick_win = True
#         winner = "Player 2"
#     elif board_state[0][2] == "|O|" and board_state[1][2] == "|O|" and board_state[2][2] == "|O|":
#         tick_win = True
#         winner = "Player 2"
#     elif board_state[0][0] == "|O|" and board_state[1][1] == "|O|" and board_state[2][2] == "|O|":
#         tick_win = True
#         winner = "Player 2"
#     elif board_state[2][0] == "|O|" and board_state[1][1] == "|O|" and board_state[0][2] == "|O|":
#         tick_win = True
#         winner = "Player 2"

    # tick_win_list = []
    # for i in range(len(board_state)):
    #     for j in range(len(board_state[i])):
    #         if board_state[i][j]== "|X|":
    #             tick_win_list.append(1)
    #         elif board_state[i][j]== "|O|":
    #             tick_win_list.append(2)
    #         else:
    #             tick_win_list.append(0)
    # print(tick_win_list)
    # if tick_win_list == [1,1,1,0,0,0,0,0,0]:
    #     tick_win = True
    #     winner = "Player 1"


# Create TicTacToe board
TTT = """
           A B C
        1 |_|_|_|
        2 |_|_|_|
        3 |_|_|_|
                      
         TO PLACE TOKEN IN TOP LEFT: A1
         TO PLACE TOKEN IN BOTTOM RIGHT: C3
        """

# Ask for player input
# PLAYER 1: X
# PLAYER 2: O
# Prompt player to reenter choice if location already occupied
board_totally_filled = False
tick_win = False
winner = ""

x_cor = 0
y_cor = 0

while not board_totally_filled and not tick_win:
    # print("TOP OF LOOP")
    print(TTT)
    update_board()

    p1 = input("PLAYER1- Please choose a location to place your token: ").upper()
    coordinate_input(p1)
    # clear()
    # print(TTT)
    try:
        while board_state[x_cor][y_cor] != "|_|":
            p1 = input("PLAYER1- Please choose a location to place your token: ").upper()
            coordinate_input(p1)
            print(board_totally_filled)
    except KeyError:  # HOW TO KEEP ASKING FOR INPUT IF KEY ERROR? But dont want nested loop in loop for 2 players...
        p1 = input("PLAYER1- Please choose a location to place your token: ").upper()
    else:
        if board_state[x_cor][y_cor] == "|_|":
            board_state[x_cor][y_cor] = "|X|"
        update_board()
        print(f"ttt- {tic_tac_win(board_state)}")
        if tic_tac_win(board_state) == "|X|":
            tick_win = True
            print("PLAYER 1 WINS!")
        elif tic_tac_win(board_state) == "|O|":
            tick_win = True
            print("PLAYER 2 WINS!")
        else:
            tick_win = False

    if tick_win:
        break

    print("CHECKING WHETHER BOARD IS FILLED")
    is_board_filled()
    if board_totally_filled:
        break

    p2 = input("PLAYER2- Please choose a location to place your token: ").upper()
    coordinate_input(p2)
    # clear()
    # print(TTT)
    try:
        while board_state[x_cor][y_cor] != "|_|":
            p2 = input("PLAYER2- Please choose a location to place your token: ").upper()
            coordinate_input(p2)
    except KeyError:
        p2 = input("PLAYER1- Please choose a location to place your token: ").upper()
    else:
        if board_state[x_cor][y_cor] == "|_|":
            board_state[x_cor][y_cor] = "|O|"
        update_board()
        print(f"ttt- {tic_tac_win(board_state)}")
        if tic_tac_win(board_state)=="|X|":
            tick_win = True
            print("PLAYER 1 WINS!")
        elif tic_tac_win(board_state)=="|O|":
            tick_win = True
            print("PLAYER 2 WINS!")
        else:
            tick_win = False
    print(f"tick_win= {tick_win}\n")

# if tick_win:
#     print(f"Winner is {winner}!")

#     #BUG ...if 1st location is rightmost. a1a2(c3)/03(8)
#     #OH... NEED WRAP PARENTHESES FOR MULTIPLE and? But still triggering --- seems like need to assign individually ...
