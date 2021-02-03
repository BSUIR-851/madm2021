from point import Point


class Cluster:
	def __init__(self):
		self._points = []
		self.cur_x = 0
		self.cur_y = 0
		self.last_x = 0
		self.last_y = 0

	def init_center(self, count, cluster_list, point_list):
		size = len(point_list)
		step = size / count
		steper = 0

		for i in range(count):
			cluster_list[i] = Cluster()
			cluster_list[i].cur_x = point_list[steper].x
			cluster_list[i].cur_y = point_list[steper].y

	def set_center(self):
		sum_x = 0
		sum_y = 0
		size = len(self._points)
		for i in range(size):
			sum_x += self._points[i].x
			sum_y += self._points[i].y

		self.last_x = self.cur_x
		self.last_y = self.cur_y

		self.cur_x = sum_x / size
		self.cur_y = sum_y / size

	def clear_points(self):
		self._points.clear()

	def add_point(self, point):
		self._points.append(point)

	def bind(self, count, cluster_list, point_list):
		for i in range(count):
			cluster_list[i].clear_points()

		size = len(point_list)

		for i in range(size):
			part1 = (cluster_list[0].cur_x - point_list[i].x) ** 2
			part2 = (cluster_list[0].cur_y - point_list[i].y) ** 2
			minimal = (part1 + part2) ** (1/2)
			cluster = cluster_list[0]

			for j in range(1, count):
				part1_tmp = (cluster_list[j].cur_x - point_list[i].x) ** 2
				part2_tmp = (cluster_list[j].cur_y - point_list[i].y) ** 2
				tmp = (part1 + part2) ** (1/2)

				if minimal > tmp:
					minimal = tmp
					cluster = cluster_list[j]

			cluster.add_point(point_list[i])

		return cluster_list

	def start(self, count, cluster_list, point_list):
		self.init_center(count, cluster_list, point_list)

		while True:
			check = 0
			self.bind(count, cluster_list, point_list)
			for i in range(count):
				cluster_list[i].set_center()

			for i in range(count):
				if (cluster_list[i].cur_x == cluster_list[i].last_x) and (cluster_list[i].cur_y == cluster_list[i].last_y):
					check += 1

			if check == count:
				return















