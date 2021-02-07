from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from random import randrange

from maxmin_view import Ui_form_maxmin

from cluster import Cluster
from point import Point


class MaxMinController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()
		self.__init_scene()
		self.__init_colors()

		self.point_list = []
		self.cluster_list = []
		self.point_size = (1, 1)

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_maxmin()
		self.ui.setupUi(self.form)

	def __init_scene(self):
		self.canvas_width = 450
		self.canvas_height = 450
		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, self.canvas_width, self.canvas_height)
		self.ui.gv_canvas.setScene(self.scene)

	def __init_colors(self):
		self.colors = [
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

	def start(self):
		self.ui.pb_generate.clicked.connect(self.__pb_generate_click)
		self.ui.pb_start.clicked.connect(self.__pb_start_click)

		self.__update_form()
		sys.exit(self.app.exec_())

	def __update_form(self):
		self.form.hide()
		self.form.show()

	def __msgbox_message(self, title, message):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setText(title)
		msgBox.setInformativeText(
			message
		)
		msgBox.exec_()

	def __generate_points(self, amount_of_points):
		points = []
		for i in range(amount_of_points):
			point = Point(randrange(self.canvas_width), randrange(self.canvas_height))
			points.append(point)
		return points

	def __draw_cluster_list(self):
		for i, cluster in enumerate(self.cluster_list):
			color = self.colors[i % len(self.colors)]
			for point_index, point in enumerate(cluster.points):
				self.__draw_point(point, color)
				center_point = Point(cluster.center_point.x, cluster.center_point.y)
				self.__draw_point(center_point, QtGui.QColor('black'))

	def __draw_point(self, point, color):
		pen = QtGui.QPen(color)
		brush = QtGui.QBrush(color)
		self.scene.addRect(point.x, point.y, self.point_size[0], self.point_size[1], pen, brush)

	def __pb_generate_click(self):
		self.scene.clear()

		try:
			amount_of_points = int(self.ui.le_amount_of_points.text())
		except ValueError:
			amount_of_points = 10000

		self.point_list = self.__generate_points(amount_of_points)

		for point in self.point_list:
			self.__draw_point(point, QtGui.QColor('black'))

	def __pb_start_click(self):
		try:
			amount_of_points = int(self.ui.le_amount_of_points.text())
		except ValueError:
			amount_of_points = 10000

		if not self.point_list:
			self.point_list = self.__generate_points(amount_of_points)

		Cluster.start(self.cluster_list, self.point_list)
		self.__draw_cluster_list()

if __name__ == '__main__':
	max_min_controller = MaxMinController()
	max_min_controller.start()





















