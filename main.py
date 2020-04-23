import time, random, colorama
from termcolor import *
colorama.init()

# Declare our game variables....
global p1, p2, signs, p1_sign, p2_sign, moves, turn, items, winner_horizontal, winner_vertical, winner_diagonal
global all_horizontal, all_vertical, all_diagonal
global items, gamePlay, boardList
boardList = ['0','1','2','3','4','5','6','7','8']

def draw_board(items):
    print('    |    |    ')
    print(' {}  | {}  | {} '.format(items[6], items[7], items[8]))
    print('____|____|____')
    print('    |    |    ')
    print(' {}  | {}  | {} '.format(items[5], items[4], items[3]))
    print('____|____|____')
    print('    |    |    ')
    print(' {}  | {}  | {} '.format(items[0], items[1], items[2]))
    print('    |    |    ')

def add_to_board(board_list, item, position):
	board_list[position] = item

def all_horizontal(items):
# All horizontal
	return items[0] == items[1] == items[2] or items[3] == items[4] == items[5] or items[6] == items[7] == items[7]
	
def all_vertical(items):
	# All vertical
	return items[0] == items[5] == items[6]  or items[1] == items[4] == items[7] or items[2] == items[3] == items[8]:

def all_diagonal(items):
	global winner_diagonal, winner_diagonal, winner_vertical
	global all_diagonal, all_diagonal, all_vertical
	# All diagonal
	return items[0] == items[4] == items[8] or items[2] == items[4] == items[6]

def start_game():
	global turn, p1_sign, p2_sign, start, p1, p2
	cprint('Welcome to TIC-TAC', 'yellow')
	print('')
	cprint('RULES:\nFirst player to make a horizontal,vertical,or diagonal line with their sign wins\nPlayers make one move at a time', 'red')
	print('')
	signs = ['X', '0']
	p1 = input('Player 1 should enter his/her name: ')
	p2 = input('Player 2 should enter his/her name: ')
	start = input('Who starts the game?(p1/p2/): ')
	signs = ['X', '0']
	p1_sign = random.choice(signs)
	if p1_sign == 'X':
		p2_sign = '0' 
	else:
		p2_sign = 'X'

	turn = start

	play_game()

def play_game():
	moves = 0
	turn  = start
	gamePlay = True
	replay = True
	global retry, boardList
	if replay == True:
		boardList = ['0','1','2','3','4','5','6','7','8']

	cprint("Player 1's sign is {}".format(p1_sign), 'yellow')
	cprint("Player 2's sign is {}".format(p2_sign), 'yellow')
	while gamePlay:
		cprint("It is {}'s turn to play".format(turn), 'red')
		print('')
		draw_board(boardList)
		loc = int(input('Which location would {} enter their sign?: '.format(turn)))

		try:
			if boardList[loc] == str(loc):
				if turn == 'p1':
					add_to_board(boardList, p1_sign, loc)
					turn = 'p2'
				else:
					add_to_board(boardList, p2_sign, loc)
					turn = 'p1'
			else:
				cprint('That space is already occupied!', 'red')

		except IndexError:
			cprint('That number is not in the board!', 'red')

		if all_horizontal(boardList) or all_vertical(boardList) or all_diagonal(boardList):
			if turn == 'p1':
				cprint('{} has won!'.format(p2), 'red')
				draw_board(boardList)
				retry = input('Do you want to retry?(yes/no): ')
				if retry == 'yes':
					replay = True
					continue
				else:
					gamePlay = False
			else:
				cprint('{} has won!'.format(p1), 'red')
				draw_board(boardList)
				retry = input('Do you want to retry?(yes/no): ')
				if retry == 'yes':
					replay = True
					continue
				else:
					gamePlay = False

if __name__ == '__main__':
	start_game()