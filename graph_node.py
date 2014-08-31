class GraphNode:

	def __init__(self, name, coordinate):
		self.neighbours = []
		self.name = name
		self.x = coordinate[0]
		self.y = coordinate[1]

	def add_neighbour(self, coordinate):
		self.neighbours.append(coordinate)
		return coordinate

	def remove_neighbour(self, coordinate):
		try:
			self.neighbours.remove(coordinate)
			return True
		except:
			return False

