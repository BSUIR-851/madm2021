from point import Point
from random import choice

from cluster import Cluster as ClusterKMeans


class ClusterMaxMin(ClusterKMeans):
	def __init__(self, center_point):
		self.points = []
		self.center_point = center_point

	def clear_points(self):
		self.points.clear()

	def add_point(self, point):
		self.points.append(point)

	@staticmethod
	def find_distance(point_1, point_2):
		part1 = (point_1.x - point_2.x) ** 2
		part2 = (point_1.y - point_2.y) ** 2
		return (part1 + part2) ** (1 / 2)

	@classmethod
	def find_max_distant_point(cls, cluster_list, point_list):
		distant_point = point_list[0]
		max_distance = 0

		for cluster in cluster_list:
			for point in cluster.points:
				distance = cls.find_distance(cluster.center_point, point)
				if distance > max_distance:
					max_distance = distance
					distant_point = point

		return max_distance, distant_point 

	@classmethod
	def bind(cls, cluster_list, point_list):
		for cluster in cluster_list:
			cluster.clear_points()

		size = len(point_list)

		for point in point_list:
			minimal = cls.find_distance(cluster_list[0].center_point, point)
			cluster = cluster_list[0]

			for j in range(1, len(cluster_list)):
				tmp = cls.find_distance(cluster_list[j].center_point, point)

				if minimal > tmp:
					minimal = tmp
					cluster = cluster_list[j]

			cluster.add_point(point)

		return cluster_list

	@classmethod
	def average_distance(cls, cluster_list):
		sum_ = 0
		amount = 0
		size = len(cluster_list)
		for i in range(size):
			for j in range(i + 1, size):
				sum_ += cls.find_distance(cluster_list[i].center_point, cluster_list[j].center_point)
				amount += 1
		return sum_/amount

	@classmethod
	def start(cls, cluster_list, point_list):
		cluster = cls(choice(point_list))
		cluster.points.extend(point_list)
		cluster_list.append(cluster)
		max_distance, new_center = cls.find_max_distant_point(cluster_list, point_list)
		cluster_list.append(cls(new_center))

		cls.bind(cluster_list, point_list)

		while True:
			max_distance, potential_center = cls.find_max_distant_point(cluster_list, point_list)
			if max_distance > (cls.average_distance(cluster_list) / 2):
				cluster_list.append(cls(potential_center))
				cls.bind(cluster_list, point_list)
			else:
				break















