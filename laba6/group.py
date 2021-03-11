from distance import Distance


class Group:
	def __init__(self):
		self.distances = []
		self.sub_groups = []
		self.name = ''
		self.x = 0.0
		self.y = 0.0

	def get_distance(self, group):
		for distance in self.distances:
			if distance.group is group:
				return distance.distance
		return -1

	def delete_distances(self, to_delete_group_list):
		for to_delete_group in to_delete_group_list:
			to_delete_distances = []
			for distance in self.distances:
				if distance.group is to_delete_group:
					to_delete_distances.append(distance)

			for to_delete_distance in to_delete_distances:
				self.distances.remove(to_delete_distance)
