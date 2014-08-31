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
	words = []
	root = board.graph[coordinate]
	if trie.child_exists(root.name):
		base_string = root.name
		for neighbour in root.neighbours:

			children = trie.get_children()
			if len(children) > 0:

def prefix_search(trie, board, coordinate, prefix):
	if len(prefix) > 0:
	else:
		trie.




board = Graph(generate_board('board.txt'))

board.find_and_add_neighbours()
