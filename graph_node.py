class GraphNode:

	def __init__(self, name, coordinates):
		self.neighbours = []
		self.name = name
		self.x = coordinates[0]
		self.y = coordaintes[1]

	def add_neighbour(self, coordinates):
		self.neighbours.append(coordinates)
		return coordinates

	def remove_neighbour(self, coordinates):
		

