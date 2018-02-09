import numpy as np

#This is a board Maker

class   Board(object):

	def __init__(self):
		self.timer = 0.5

	def num_alpha(self, num):
		alpha = ['O', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
		if num >= 1 and num < 8:
			return alpha[num]
		else:
			return ("NO PLACE FOUND")
	
	def	return_position(self, alpha, num):
		if alpha == "NO PLACE FOUND":
			return ("CAN'T FIND POSITION")
		else:
			return (str(num) + alpha)

	def set_board(self):
		dic = {  0: [0, 1, 2, 3, 4, 5, 6, 7],
				 1: [0, 1, 2, 3, 4, 5, 6, 7],
				 2: [0, 1, 2, 3, 4, 5, 6, 7],
				 3: [0, 1, 2, 3, 4, 5, 6, 7],
				 4: [0, 1, 2, 3, 4, 5, 6, 7],
				 5: [0, 1, 2, 3, 4, 5, 6, 7],
				 6: [0, 1, 2, 3, 4, 5, 6, 7],
				 7: [0, 1, 2, 3, 4, 5, 6, 7],
		}
		return (dic)

	def print_board(self, board):
		cnt = 0
		cnt2 = 0;
		while cnt <= 7:
			while cnt2 <= 7:
				print(board[cnt][cnt2], end='')
				print(' ', end='')
				cnt2 += 1
			print('\n')
			cnt2 = 0
			cnt += 1

b = Board()
board1 = b.set_board()
board1[1][0] = 'K'