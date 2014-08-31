from graph_node import GraphNode as Node
from trie import Trie

class Graph:

	def __init__(self, graph_array = None):
		self.graph = {}
		self.populate_graph(graph_array)

	def populate_graph(self, graph_array):
		if graph_array is not None:
			for row_index, row in enumerate(graph_array):
				for node_index, node in enumerate(row):
					self.set_node((node_index, row_index), node)
			return True
		else:
			return False

	def set_node(self, coordinate, char):
		self.graph[coordinate] = Node(char, coordinate)
		return self.graph[coordinate]

	def get_node(self, coordinate):
		node = self.graph.get(coordinate, None)
		if node is not None:
			return self.graph[coordinate]
		else:
			return None

	def print_graph(self):
		for key, value in self.graph.items():
			print(key, value, value.name)

	def add_neighbours(self, node_coordinate, coordinates):
		for coordinate in coordinates:
			self.graph[node_coordinate].add_neighbour(coordinate)

	def find_and_add_neighbours(self):
		count = 0
		for key in self.graph:
			neighbours = []
			for coordinate in self.graph:
				if abs(key[0] - coordinate[0]) <= 1 and abs(key[1] - coordinate[1]) <= 1:
					if not key == coordinate:
						neighbours.append(coordinate)
			self.add_neighbours(key, neighbours)