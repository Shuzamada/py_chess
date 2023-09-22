from stockfish import Stockfish
import time

stockfish = Stockfish(path = 'D:\ches\stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe')
stockfish.set_fen_position("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1")




move_number = 0

def convert_move(str_move):
	letters = ['a','b','c','d','e','f','g','h']

	if len(str_move) == 5:
		start_x = letters.index(str_move[0])
		start_y = int(str_move[1]) - 1
		end_x = letters.index(str_move[3])
		end_y = int(str_move[4]) - 1
	else:
		start_x = letters.index(str_move[0])
		start_y = int(str_move[1]) - 1
		end_x = letters.index(str_move[2])
		end_y = int(str_move[3]) - 1

	return start_x, start_y, end_x, end_y

class ChessMan(object):

	model = None

	def __init__(self, color):
		self.color = color

	def __str__(self):
		return self.model[1 if self.color == Color.WHITE else 0]

class Color():
	EMPTY = 0	
	BLACK = 1
	WHITE = 2

class Empty(object):
	color = Color.EMPTY

	def get_moves(self, board, x, y):
		raise Exception('Error !')

	def __str__(self):
		return '.'


class Pawn(ChessMan):
	model = ['♙ ','♟']
	didnt_move = 1

	def get_moves(self, board, x, y):
		moves = []
		if self.color == Color.WHITE:
			if self.didnt_move == 1:
				if board.board[x][y + 2].color == Color.EMPTY and board.board[x][y + 1].color == Color.EMPTY:
					moves.append((x, y + 2))
			if board.board[x][y + 1].color == Color.EMPTY: 
				moves.append((x, y + 1))
			if x < 7 and board.board[x + 1][y + 1].color == Color.BLACK:
				moves.append((x + 1, y + 1))
			if x > 0 and board.board[x - 1][y + 1].color == Color.BLACK:
				moves.append((x - 1, y + 1))


		elif self.color == Color.BLACK:
			if self.didnt_move == 1:
				if board.board[x][y - 2].color == Color.EMPTY and board.board[x][y - 1].color == Color.EMPTY:
					moves.append((x, y - 2))
			if board.board[x][y - 1].color == Color.EMPTY: 
				moves.append((x, y - 1))
			if x < 7 and board.board[x + 1][y - 1].color == Color.WHITE:
				moves.append((x + 1, y - 1))
			if board.board[x - 1][y - 1].color == Color.WHITE:
				moves.append((x - 1, y - 1))
		return moves


class Knight(ChessMan):
	model = ['♘', '♞']

	def get_moves(self, board, x, y):
		moves = []
		if x + 2 < 8 and y + 1 < 8:
			moves.append((x + 2, y + 1)) if (board.board[x + 2][y + 1].color == Color.EMPTY or board.board[x + 2][y + 1].color != board.board[x][y].color) else None
		if x + 2 < 8 and y - 1 >= 0:
			moves.append((x + 2, y - 1)) if (board.board[x + 2][y - 1].color == Color.EMPTY or board.board[x + 2][y - 1].color != board.board[x][y].color)  else None
		if x - 2 >= 0 and y + 1 < 8:
			moves.append((x - 2, y + 1)) if (board.board[x - 2][y + 1].color == Color.EMPTY or board.board[x - 2][y + 1].color != board.board[x][y].color)  else None
		if x - 2 >= 0 and y + 1 >= 0:
			moves.append((x - 2, y - 1)) if (board.board[x - 2][y - 1].color == Color.EMPTY or board.board[x - 2][y - 1].color != board.board[x][y].color)  else None
		if x + 1 < 8 and y + 2 < 8:
			moves.append((x + 1, y + 2)) if (board.board[x + 1][y + 2].color == Color.EMPTY or board.board[x + 1][y + 2].color != board.board[x][y].color)  else None
		if x + 1 < 8 and y - 2 >= 0:
			moves.append((x + 1, y - 2)) if (board.board[x + 1][y - 2].color == Color.EMPTY or board.board[x + 1][y - 2].color != board.board[x][y].color)  else None
		if x - 1 >= 0 and y + 2 < 8:
			moves.append((x - 1, y + 2)) if (board.board[x - 1][y + 2].color == Color.EMPTY or board.board[x - 1][y + 2].color != board.board[x][y].color)  else None
		if x - 1 >= 0 and y - 2 >= 0:
			moves.append((x - 1, y - 2)) if (board.board[x - 1][y - 2].color == Color.EMPTY or board.board[x - 1][y - 2].color != board.board[x][y].color)  else None

		
		return moves

class Bishop(ChessMan):
	model = ['♗','♝']

	def get_moves(self, board, x, y):
		moves = []

		for i in range(1,8):		
			if x + i < 8 and y + i < 8:	

				if board.board[x + i][y + i].color == Color.EMPTY:
						moves.append((x + i, y + i)) 
				elif board.board[x + i][y + i].color != board.board[x][y].color:	
						moves.append((x + i, y + i))
						break
				elif board.board[x + i][y + i].color == board.board[x][y].color:
					break	


		for i in range(1,8):		
			if x + i < 8 and y - i >= 0:	
				if board.board[x + i][y - i].color == Color.EMPTY:
						moves.append((x + i, y - i)) 
				elif board.board[x + i][y - i].color != board.board[x][y].color:	
						moves.append((x + i, y - i))
						break
				elif board.board[x + i][y - i].color == board.board[x][y].color:
					break	
		for i in range(1,8):		
			if x - i >= 0 and y + i < 8:	
				if board.board[x - i][y + i].color == Color.EMPTY:
						moves.append((x - i, y + i)) 
				elif board.board[x - i][y + i].color != board.board[x][y].color:	
						moves.append((x - i, y + i))
						break
				elif board.board[x - i][y + i].color == board.board[x][y].color:
					break	

		for i in range(1,8):		
			if x - i >= 0 and y - i >= 0:	
				if board.board[x - i][y - i].color == Color.EMPTY:
						moves.append((x - i, y - i)) 
				elif board.board[x - i][y - i].color != board.board[x][y].color:	
						moves.append((x - i, y - i))
						break
				elif board.board[x - i][y - i].color == board.board[x][y].color:
					break	

		return moves	

class Rock(ChessMan):
	model = ['♖','♜']

	def get_moves(self, board, x, y):
		moves = []

		for i in range(x - 1, -1, -1):
			if board.board[i][y].color == Color.EMPTY:
				moves.append((i, y))
			elif board.board[i][y].color != board.board[x][y].color:
				moves.append((i,y))
				break
			elif board.board[i][y].color == board.board[x][y].color:
				break

		for i in range(x + 1, 8):
			if board.board[i][y].color == Color.EMPTY:
				moves.append((i, y))
			elif board.board[i][y].color != board.board[x][y].color:
				moves.append((i,y))
				break
			elif board.board[i][y].color == board.board[x][y].color:
				break

		for i in range(y - 1, -1, -1):
			if board.board[x][i].color == Color.EMPTY:
				moves.append((x, i))
			elif board.board[x][i].color != board.board[x][y].color:
				moves.append((x,i))
				break
			elif board.board[x][i].color == board.board[x][y].color:
				break

		for i in range(y + 1, 8):
			if board.board[x][i].color == Color.EMPTY:
				moves.append((x,i))
			elif board.board[x][i].color != board.board[x][y].color:
				moves.append((x,i))
				break
			elif board.board[x][i].color == board.board[x][y].color:
				break

		return moves

class Queen(ChessMan):
	model = ['♕','♛']

	def get_moves(self, board, x, y):
		bishop_moves = Bishop(self.color)
		rock_moves = Rock(self.color)
		moves = rock_moves.get_moves(board, x, y) + bishop_moves.get_moves(board, x, y)
		return moves


class King(ChessMan):
	model = ['♔','♚']

	def get_moves(self, board, x, y):
		moves = []
		for j in (y-1, y, y+1):
			for i in (x-1, x, x+1):
				if i == x and j == y:
					continue
				if 0 <= i <= 7 and 0 <= j <= 7 and board.board[x][y].color != self.color:
					moves.append([i, j])
		return moves


class Board():

	def __init__(self):
		self.move_number = 0
		self.board = [[Empty()] * 8 for i in range(8)]

		
		for i in range(8):
			self.board[i][1] = Pawn(Color.WHITE)
		self.board[0][0] = Rock(Color.WHITE)
		self.board[1][0] = Knight(Color.WHITE)
		self.board[2][0] = Bishop(Color.WHITE)
		self.board[3][0] = Queen(Color.WHITE)
		self.board[4][0] = King(Color.WHITE)
		self.board[5][0] = Bishop(Color.WHITE)
		self.board[7][0] = Rock(Color.WHITE)
		self.board[6][0] = Knight(Color.WHITE)
	

		for i in range(8):
			self.board[i][6] = Pawn(Color.BLACK)
		self.board[0][7] = Rock(Color.BLACK)
		self.board[1][7] = Knight(Color.BLACK)
		self.board[2][7] = Bishop(Color.BLACK)
		self.board[3][7] = Queen(Color.BLACK)
		self.board[4][7] = King(Color.BLACK)
		self.board[5][7] = Bishop(Color.BLACK)
		self.board[7][7] = Rock(Color.BLACK)
		self.board[6][7] = Knight(Color.BLACK)
	


	def __str__(self):
		res = ''
		numbers = ' 87654321'
		for i in range(1,9):
			res += numbers[i]
			for j in range(8):
				if isinstance(self.board[j][-i],Pawn):
					res += str(self.board[j][-i])
				else:
					res += str(self.board[j][-i]) + ' '
			res += '\n'
		res += ' A B C D E F G H'
		return res


		return res
	def get_moves(self, x, y):
		return self.board[x][y].get_moves(board, x, y)

	def get_all_moves(self):
		moves = []
		for x in range(8):
			for y in range(8):
				if not (isinstance(self.board[x][y],Empty)):
					now_moves = self.get_moves(x, y)
					moves.append(now_moves) if now_moves else None
		return moves

	def	move(self, str_move):
		start_x, start_y, end_x, end_y = convert_move(str_move)

		if isinstance(self.board[start_x][start_y], Empty):
			return('illegal move, empty field')
		if self.board[start_x][start_y].color == Color.BLACK and self.move_number % 2 == 0:
			return('illegal move, now white moves')
		if self.board[start_x][start_y].color == Color.WHITE and self.move_number % 2 == 1:
			return('illegal move, now black moves')	

		if (end_x, end_y) in self.get_moves(start_x, start_y):
			self.board[end_x][end_y] = self.board[start_x][start_y] 
			self.board[start_x][start_y] = Empty()


			self.move_number += 1
			return(board)
		else:
			return('illegal move')



board = Board()
move_number = 0



print(board)
print('')
print('enter your move' + '\n' + 'example: e2-e4' + '\n')


while True:
	if move_number % 2 == 0:
		str_move = str(input()).lower()
		print('')
		if isinstance(board.move(str_move), Board):
			stockfish.make_moves_from_current_position([str_move.replace('-','')])
			print(board)
			move_number += 1
		else:
			print(board.move(str_move))
		print('')
		
		
		

	else:
		ai_move = stockfish.get_best_move()
		
		stockfish.make_moves_from_current_position([ai_move])
		print(board.move(ai_move))
		move_number += 1

