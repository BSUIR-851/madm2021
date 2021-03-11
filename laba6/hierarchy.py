from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

from distance import Distance
from group import Group
from point import Point


class Hierarchy(object):
	def __init__(self, distances, size):
		self.__init_colors()
		self.__groups = []
		self.__offset_x = 1.0
		self.__temp_color = 0
		self.__temp_char = 0

		for i in range(size):
			new_group = Group()
			new_group.name = 'x{}'.format(i + 1)
			self.__groups.append(new_group)

		for i in range(len(self.__groups)):
			for j in range(len(self.__groups)):
				if i != j:
					self.__groups[i].distances.append(Distance(distances[i][j], self.__groups[j]))

	def __init_colors(self):
		self.__colors = [
			QtGui.QColor('aqua'),
			QtGui.QColor('bisque'),
			QtGui.QColor('blue'),
			QtGui.QColor('blueviolet'),
			QtGui.QColor('burlywood'),
			QtGui.QColor('crimson'),
			QtGui.QColor('darkblue'),
			QtGui.QColor('darkgray'),
			QtGui.QColor('darkgreen'),
			QtGui.QColor('darkmagenta'),
			QtGui.QColor('darkred'),
			QtGui.QColor('darksalmon'),
			QtGui.QColor('darkseagreen'),
			QtGui.QColor('deeppink'),
			QtGui.QColor('forestgreen'),
			QtGui.QColor('gold'),
			QtGui.QColor('lightpink'),
			QtGui.QColor('orange'),
			QtGui.QColor('plum'),
			QtGui.QColor('teal'),
		]

	def __add_groups(self, added_groups, min_distance):
		new_group = Group()
		new_group.name = self.__next_char()
		for group in self.__groups:
			if group not in added_groups:
				min_distance_temp = group.get_distance(added_groups[0])

				for curr_group in added_groups:
					if group.get_distance(curr_group) < min_distance_temp:
						min_distance_temp = group.get_distance(curr_group)

				group.delete_distances(added_groups)
				group.distances.append(Distance(min_distance_temp, new_group))
				new_group.distances.append(Distance(min_distance_temp, group))

		for added_group in added_groups:
			if added_group.x == 0.0:
				added_group.x = self.__offset_x
				self.__offset_x += 1


		new_group.sub_groups = added_groups

		sub_groups_points = []
		for added_group in added_groups:
			sub_groups_points.append(Point(added_group.x, added_group.y))
			try:
				self.__groups.remove(added_group)
			except ValueError:
				print('group has been deleted before')

		x = 0.0
		for point in sub_groups_points:
			x += point.x

		new_group.x = x / len(sub_groups_points)
		new_group.y = min_distance
		self.__groups.append(new_group)

	def __next_char(self):
		self.__temp_char += 1
		return chr(ord('a') + self.__temp_char - 1)

	def find_groups(self):
		result = True

		while result:
			result = False
			min_distance = 1000.0
			groups_with_min_distance = []

			for group in self.__groups:
				for distance in group.distances:
					if distance.distance <= min_distance:
						if distance.distance < min_distance:
							min_distance = distance.distance
							result = True
							groups_with_min_distance.clear()
						groups_with_min_distance.append(group)

			if result and (len(groups_with_min_distance) > 1):
				self.__add_groups(groups_with_min_distance, min_distance)

	def __clear_axes(self, chart):
		for axis in chart.axes():
			chart.removeAxis(axis)

	def __set_default_chart(self, chart):
		chart.removeAllSeries()
		self.__clear_axes(chart)

		axis_x = QtChart.QValueAxis()
		axis_x.setTitleText('')
		axis_x.setRange(-1, self.__offset_x + 1)

		axis_y = QtChart.QValueAxis()
		axis_y.setTitleText('')
		axis_y.setRange(-1, self.__groups[0].y + 1)

		chart.setAxisX(axis_x)
		chart.setAxisY(axis_y)

	def __draw_groups(self, chart, group):
		result = True
		for curr_series in chart.series():
			if curr_series.name() == group.name:
				result = False
				break

		if result:
			points_series = QtChart.QScatterSeries()
			points_series.setName(group.name)
			points_series.setMarkerSize(10)
			points_series.setBorderColor(self.__colors[self.__temp_color % len(self.__colors)])
			self.__temp_color += 1
			points_series.append(group.x, group.y)

			if points_series not in chart.series():
				chart.addSeries(points_series)

			for sub_group in group.sub_groups:
				line_series = QtChart.QLineSeries()
				line_series.setName(group.name + ' ' + sub_group.name)
				line_series.setColor(points_series.borderColor())
				line_series.append(sub_group.x, sub_group.y)
				line_series.append(sub_group.x, group.y)
				line_series.append(group.x, group.y)
				result = True

				for curr_series in chart.series():
					if curr_series.name() == line_series.name():
						result = False
						break
						
				if result:
					chart.addSeries(line_series)

				self.__draw_groups(chart, sub_group)

	def draw(self, chart):
		# self.__set_default_chart(chart)
		for group in self.__groups:
			self.__draw_groups(chart, group)

