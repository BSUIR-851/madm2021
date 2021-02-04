from point import Point


class Cluster:
	def __init__(self):
		self.points = []
		self.cur_x = 0
		self.cur_y = 0
		self.last_x = 0
		self.last_y = 0

	@staticmethod
	def init_center(number_of_classes, cluster_list, point_list):
		size = len(point_list)
		step = size // number_of_classes
		steper = 0

		for cluster in cluster_list:
			cluster.cur_x = point_list[steper].x
			cluster.cur_y = point_list[steper].y
			steper += step

	def set_center(self):
		sum_x = 0
		sum_y = 0
		size = len(self.points)

		for point in self.points:
			sum_x += point.x
			sum_y += point.y

		self.last_x = self.cur_x
		self.last_y = self.cur_y

		self.cur_x = sum_x / size
		self.cur_y = sum_y / size

	def clear_points(self):
		self.points.clear()

	def add_point(self, point):
		self.points.append(point)

	@staticmethod
	def bind(number_of_classes, cluster_list, point_list):
		for cluster in cluster_list:
			cluster.clear_points()

		size = len(point_list)

		for point in point_list:
			part1 = (cluster_list[0].cur_x - point.x) ** 2
			part2 = (cluster_list[0].cur_y - point.y) ** 2
			minimal = (part1 + part2) ** (1 / 2)
			cluster = cluster_list[0]

			for j in range(1, number_of_classes):
				part1_tmp = (cluster_list[j].cur_x - point.x) ** 2
				part2_tmp = (cluster_list[j].cur_y - point.y) ** 2
				tmp = (part1_tmp + part2_tmp) ** (1 / 2)

				if minimal > tmp:
					minimal = tmp
					cluster = cluster_list[j]

			cluster.add_point(point)

		return cluster_list

	@classmethod
	def start(cls, number_of_classes, cluster_list, point_list):
		cls.init_center(number_of_classes, cluster_list, point_list)

		while True:
			check = 0
			cls.bind(number_of_classes, cluster_list, point_list)

			for cluster in cluster_list:
				cluster.set_center()

			for cluster in cluster_list:
				if (cluster.cur_x == cluster.last_x) and (cluster.cur_y == cluster.last_y):
					check += 1

			if check == number_of_classes:
				return















