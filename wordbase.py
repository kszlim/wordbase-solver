from graph import Graph
from trie import Trie

trie = Trie()

trie.populate_trie('wordlist.txt')

def generate_board(file_name):
		
	with open(file_name) as board_string:
		board_string = board_string.read()
		board = []
		for i in range(0, len(board_string), 10):
			board.append(board_string[i:i+10])
		return board

def look_for_words(trie, board, coordinate):
	pass

def words_at_coordinate(trie, board, coordinate):

board = Graph(generate_board('board.txt'))

board.find_and_add_neighbours()
