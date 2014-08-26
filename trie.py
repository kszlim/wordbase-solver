from node import Node

class Trie:

	def __init__(self):
		self.root = Node(None)

	def add_string(self, string):
		node = self.root
		for char in enumerate(string):
			node = node.add_child(char)

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