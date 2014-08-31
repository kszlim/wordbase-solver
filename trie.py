from node import Node

class Trie:

	def __init__(self):
		self.root = Node(None)

	def add_string(self, string):
		node = self.root
		string_length = len(string)
		for index, char in enumerate(string):
			node = node.add_child(char)
			#Add None to indicate end of string?
			if index == string_length - 1:
				node.add_child(None)

	def string_exists(self, string):
		node = self.root
		trie_string = ''

		for char in string:
			if not node.child_exists(char):
				break
			if node.child_exists(char):
				trie_string += node.child_exists(char).name
			node = node.child_exists(char)

		if trie_string == string:
			return True
		else:
			return False

	def populate_trie(self, file_location):
		with open(file_location) as filelist:
			for index, line in enumerate(filelist):
				self.add_string(line)
				if index % 10000 == 0:
					print(index, 'words imported')
			print('Done importing all words.')

	def get_node(self, prefix = None, node = None):
		if node is not None:
			strings = []
			node = self.root
			for char in prefix:
				if node.child_exists(char):
					node = node.children[char]
				else:
		if prefix is not None:




	# def print_words(self, string):
	# 	node = self.root
	# 	if len(string) > 0:
	# 		for child in node.children:
	# 			print_words(child)

	# 	else:
	# 		trie_string = ''
	# 		word_list = []
	# 		for char in string:
	# 			node = node.child_exists(char)
	# 			if node:
	# 				trie_string += node.name
	# 				if len(node.get_children()) > 0:
	# 					for child in node.get_children():
	# 						child_string = trie_string
	# 						child_string
	# 		for child in node.children:
