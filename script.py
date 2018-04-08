from random import randint
from time import sleep

board = []
board.append([str(i) for i in range(0,10)])
             
for x in range(1, 10):
  temp = [str(x)] + ["O"] * 9
  board.append(temp)

def print_board(board):
  for row in board:
    print(" ".join(row))

print_board(board)

def random_row(board):
  return randint(1, len(board) - 1) 

def random_col(board):
  return randint(1, len(board[0]) - 1) 

ship_row = random_row(board)
ship_col = random_col(board)
print("The battleship's row is %s." % ship_row)
print("The battleship's col is %s." % ship_col) 
c = 0
turn = 0
# Everything from here on should be in your for loop
# don't forget to properly indent!

while turn < 10000 and c == 0:
  print("The Competition Begins...")
  sleep(0.1)
  #guess_row = int(raw_input("Guess Row: ")) 
  guess_row = int(randint(1,9))
  print("The Computer2 Guess_row: %s" % guess_row)
  sleep(0.3)
  guess_col = int(randint(1,9))
  print("The Computer2 Guess_col: %s" % guess_col)
  #guess_col = int(raw_input("Guess Col: ")) 
  sleep(0.3)
  print("Result...")
  if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations! Computer2 sank the battleship!")
    board[guess_row][guess_col] = "*"
    print_board(board)
    c = 1
  else:
    if guess_row not in range(1,10) or \
      guess_col not in range(1,10) :
      print("Oops, that's not even in the ocean.")
      sleep(1)
      #if turn == 3:
        #print("Game Over")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
      sleep(0.5)
      #if turn == 3:
        #print("Game Over")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
      #if turn==3:
        #print("Game Over")
    turn += 1
    print ("This is the Competition %s" % turn)
    print_board(board)
print("The computer1 won the competition!")