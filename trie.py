from node import Node

class Trie:

	def __init__(self):
		self.root = Node(None)

	def add_string(self, string):
		node = self.root
		string_length = len(string)
		for index, char in enumerate(string):
			node = node.add_child(char)

	def string_exists(self, string):
		node = self.root
		trie_string = ''
		string += '\n'
		for char in string:
			if not node.child_exists(char):
				break
			node = node.child_exists(char)
			if node:
				trie_string += char
		
		if trie_string == string:
			return True
		else:
			return False

	def populate_trie(self, file_location):
		with open(file_location) as wordlist:
			for index, line in enumerate(wordlist):
				self.add_string(line)

	@staticmethod
	def get_node(prefix, node):
		if len(prefix) > 0:
			try:
				child = node.children[prefix.pop(0)]
				return Trie.get_node(prefix, child)
			except:
				return node
		else:
			return node