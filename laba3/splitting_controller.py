from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from random import randrange
from math import exp
from math import pi

from splitting_view import Ui_form_splitting

from point import Point


class SplittingController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()
		self.__init_scene()
		self.__init_colors()

		self.amount_of_points = 10000
		self.offset = 100
		self.scale_mode = 150000

		self.pen_width = 2
		self.point_size = (2, 2)

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_splitting()
		self.ui.setupUi(self.form)

	def __init_scene(self):
		self.canvas_width = 670
		self.canvas_height = 480
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
		self.ui.pb_calculate.clicked.connect(self.__pb_calculate_click)

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

	def __draw_point(self, point, color):
		pen = QtGui.QPen(color)
		pen.setWidth(self.pen_width)
		brush = QtGui.QBrush(color)
		self.scene.addRect(point.x, point.y, self.point_size[0], self.point_size[1], pen, brush)

	def __draw_line(self, start_point, end_point, color):
		pen = QtGui.QPen(color)
		pen.setWidth(self.pen_width)
		self.scene.addLine(start_point.x, start_point.y, end_point.x, end_point.y, pen)

	def __generate_random_point_lists(self):
		point_list_1 = []
		point_list_2 = []

		for i in range(self.amount_of_points):
			point_list_1.append(randrange(self.canvas_width) - self.offset)
			point_list_2.append(randrange(self.canvas_width) + self.offset)

		return point_list_1, point_list_2

	def __calculate_mu(self, point_list):
		mu = 0
		for point in point_list:
			mu += point
		return mu / len(point_list)

	def __calculate_sigma(self, point_list, mu):
		sigma = 0
		for point in point_list:
			sigma += (point - mu) ** 2
		return (sigma / len(point_list)) ** (1 / 2)

	def __calc_propability(self, x, mu, sigma):
		part_1 = ((x - mu) / sigma) ** 2
		part_2 = exp(-0.5 * part_1)
		p = part_2 / (sigma * ((2 * pi) ** (1 / 2)))
		return p

	def __draw_density(self, point_list, p_c, color):
		mu = self.__calculate_mu(point_list)
		sigma = self.__calculate_sigma(point_list, mu)

		for x in range(len(point_list)):
			p = self.__calc_propability(x, mu, sigma)
			self.__draw_point(Point(x, self.canvas_height - (p * p_c * self.scale_mode)), color)

	def __calculate_error_rates(self, p_c1, p_c2, point_list_1, point_list_2):
		eps = 0.001
		x = -self.offset
		p1 = 1
		p2 = 0
		mu1 = self.__calculate_mu(point_list_1)
		sigma1 = self.__calculate_sigma(point_list_1, mu1)

		mu2 = self.__calculate_mu(point_list_2)
		sigma2 = self.__calculate_sigma(point_list_2, mu2)

		false_alarm_probability = 0
		missing_error_detection_probability = 0

		if p_c2 != 0:
			while p2 < p1:
				p1 = p_c1 * self.__calc_propability(x, mu1, sigma1)
				p2 = p_c2 * self.__calc_propability(x, mu2, sigma2)
				false_alarm_probability += p2 * eps
				x += eps

		border_x = x
		while x < self.canvas_width + 100:
			p1 = self.__calc_propability(x, mu1, sigma1)
			p2 = self.__calc_propability(x, mu2, sigma2)
			missing_error_detection_probability += p1 * p_c1 * eps
			x += eps

		if (p_c1 != 0) and (p_c2 != 0):
			self.__draw_line(Point(border_x, 0), Point(border_x, self.canvas_height), self.colors[1])

		if p_c1 == 0:
			false_alarm_probability = 1
			missing_error_detection_probability = 0
		else:
			if p_c2 == 0:
				false_alarm_probability = 0
				missing_error_detection_probability = 0
			else:
				false_alarm_probability /= p_c1
				missing_error_detection_probability /= p_c1

		return false_alarm_probability, missing_error_detection_probability

	def __pb_calculate_click(self):
		self.scene.clear()
		try:
			p_c1 = float(self.ui.le_p_c1.text())
		except ValueError:
			p_c1 = 0.25

		try:
			p_c2 = float(self.ui.le_p_c2.text())
		except ValueError:
			p_c2 = 0.75

		if (p_c1 < 0) or (p_c2 < 0) or ((p_c1 + p_c2) != 1) or (p_c1 > 1) or (p_c2 > 1):
			self.__msgbox_message('Incorrect input', 'P(C1)/P(C2) must be >0, <1;\nP(C1) + P(C2) = 1')
			return

		point_list_1, point_list_2 = self.__generate_random_point_lists()

		self.__draw_density(point_list_1, p_c1, self.colors[6])
		self.__draw_density(point_list_2, p_c2, self.colors[11])

		false_alarm_probability, missing_error_detection_probability = self.__calculate_error_rates(p_c1, p_c2, point_list_1, point_list_2)
		total_error = false_alarm_probability + missing_error_detection_probability

		self.ui.le_false_alarm_probability.setText('{:.4f}'.format(false_alarm_probability))
		self.ui.le_missing_error_detection_probability.setText('{:.4f}'.format(missing_error_detection_probability))
		self.ui.le_total_error.setText('{:.4f}'.format(total_error))

if __name__ == '__main__':
	splitting_controller = SplittingController()
	splitting_controller.start()





















