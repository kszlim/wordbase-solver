from graph import Graph
from trie import Trie
from copy import deepcopy

trie = Trie()

trie.populate_trie('wordlist.txt')

def generate_board(file_name):
		
	with open(file_name) as board_string:
		board_string = board_string.read().lower()
		board = []
		for i in range(0, len(board_string), 10):
			board.append(board_string[i:i+10])
		return board

def look_for_words(trie, board, depth=8):
	return [[words_at_coordinate(trie, board, (x,y), depth) for y in range(0,13)] for x in range(0,10)]

def words_at_coordinate(trie, board, coordinate, depth, base_string=""):
	words = []

	root = board.graph[coordinate]

	if root is None:
		return words
	
	board.graph[root.name] = None

	base_string += root.name
	
	trie_node = trie.get_node(list(base_string), trie.root)
	if len(base_string) > depth:
		return words
	if trie_node:
		if trie.string_exists(base_string):
			words.append(base_string)
		children = trie_node.get_neighbour_names()
		if len(children):
			for neighbour in root.neighbours:
				for word in words_at_coordinate(trie, board, neighbour, depth, base_string):
					words.append(word)
	return words

board = Graph(generate_board('board.txt'))

board.find_and_add_neighbours()
