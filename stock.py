from stockfish import Stockfish
stockfish = Stockfish(path = 'D:\ches\stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe')
stockfish.set_fen_position("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w - 0 2")
print(stockfish.is_fen_valid("rnbqkbnr/pppp1ppp/4p3/8/4P3/8/PPPP1PPP/RNBQKBNR w - - 0 2"))

print(stockfish.get_best_move())
while 	True:
	print(stockfish.get_best_move())
	stockfish.make_moves_from_current_position([stockfish.get_best_move()])