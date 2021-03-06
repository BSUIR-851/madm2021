from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from potential_view import Ui_form_potential

from potential import Potential
from point import Point


class PotentialController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()
		self.__init_scene()
		self.__init_colors()

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_potential()
		self.ui.setupUi(self.form)

	def __init_scene(self):
		self.__step = 40

		self.__pen_width = 1
		self.__point_width = 4
		self.__point_height = 4

		self.__canvas_width = self.ui.gv_graphic.size().width() - 10
		self.__canvas_height = self.ui.gv_graphic.size().height() - 10

		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, self.__canvas_width, self.__canvas_height)
		self.ui.gv_graphic.setScene(self.scene)

	def __init_colors(self):
		self.__colors = [
			QtGui.QColor('gray'),
			QtGui.QColor('purple')
		]

	def start(self):
		self.__func = None
		self.__amount_of_classes = 2

		self.__training_vectors = []
		self.__training_vectors.append([Point(3, 2), Point(-5, 0)])
		self.__training_vectors.append([Point(4, -7), Point(1, 1)])

		self.ui.pb_train.clicked.connect(self.__pb_train_click)
		self.ui.pb_classificate.clicked.connect(self.__pb_classificate_click)

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

	def __pb_train_click(self):
		try:
			class_0_point_0_x = int(self.ui.le_class_0_point_0_x.text())
			class_0_point_0_y = int(self.ui.le_class_0_point_0_y.text())
			point_0 = Point(class_0_point_0_x, class_0_point_0_y)

			class_0_point_1_x = int(self.ui.le_class_0_point_1_x.text())
			class_0_point_1_y = int(self.ui.le_class_0_point_1_y.text())
			point_1 = Point(class_0_point_1_x, class_0_point_1_y)

			self.__training_vectors[0] = [point_0, point_1]
		except ValueError:
			self.__training_vectors[0] = [Point(3, 2), Point(-5, 0)]

		try:
			class_1_point_0_x = int(self.ui.le_class_1_point_0_x.text())
			class_1_point_0_y = int(self.ui.le_class_1_point_0_y.text())
			point_0 = Point(class_1_point_0_x, class_1_point_0_y)

			class_1_point_1_x = int(self.ui.le_class_1_point_1_x.text())
			class_1_point_1_y = int(self.ui.le_class_1_point_1_y.text())
			point_1 = Point(class_1_point_1_x, class_1_point_1_y)

			self.__training_vectors[1] = [point_0, point_1]
		except ValueError:
			self.__training_vectors[1] = [Point(4, -7), Point(1, 1)]

		potential = Potential(self.__amount_of_classes)
		self.__func, isSuccess = potential.train(self.__training_vectors)
		
		if not isSuccess:
			self.__msgbox_message('Error', 'An error occurred while training. \nEnter another training data.')
		else:
			self.scene.clear()
			self.__draw_axes()
			self.__draw_graphic()
			self.__draw_training_points()

		try:
			self.ui.le_separated_function.setText(str(self.__func))
		except ValueError:
			self.__msgbox_message('Error', 'An error occurred while training. \nEnter another training data.')
	
	def __draw_point(self, point, color):
		pen = QtGui.QPen(color)
		pen.setWidth(self.__pen_width)
		brush = QtGui.QBrush(color)
		self.scene.addEllipse(point.x, point.y, self.__point_width, self.__point_height, pen, brush)

	def __draw_line(self, start_point, end_point, color):
		pen = QtGui.QPen(color)
		pen.setWidth(self.__pen_width)
		self.scene.addLine(start_point.x, start_point.y, end_point.x, end_point.y, pen)

	def __draw_axes(self):
		start_point = Point(0, self.__canvas_height / 2)
		end_point = Point(self.__canvas_width, self.__canvas_height / 2)
		self.__draw_line(start_point, end_point, QtGui.QColor('black'))

		start_point = Point(self.__canvas_width / 2, 0)
		end_point = Point(self.__canvas_width/ 2, self.__canvas_height)
		self.__draw_line(start_point, end_point, QtGui.QColor('black'))

	def __draw_graphic(self):
		self.__pen_width = 2
		step_x = 0.1
		self.__step = self.__canvas_height / 15
		start_x = (self.__canvas_width / 2) - (self.__canvas_width * self.__step / 2) 
		start_y = (self.__canvas_height / 2) - (self.__func.get_y(-self.__canvas_width / 2 / self.__step) * self.__step)
		start_point = Point(start_x, start_y)
		x = -self.__canvas_width / 2
		while x < self.__canvas_width / 2:
			y = self.__func.get_y(x / self.__step)
			curr_point = Point((self.__canvas_width / 2) + x, (self.__canvas_height / 2) - (y * self.__step))

			if abs(curr_point.y - start_point.y) < self.__canvas_height:
				self.__draw_line(start_point, curr_point, QtGui.QColor('red'))
			start_point = curr_point
			x += step_x

	def __draw_training_points(self):
		for vector_index, vector in enumerate(self.__training_vectors):
			for point in vector:
				new_coord_x = self.__canvas_width / 2 + point.x * self.__step - self.__point_width / 2
				new_coord_y = self.__canvas_height / 2 - point.y * self.__step - self.__point_height / 2
				self.__draw_point(Point(new_coord_x, new_coord_y), self.__colors[vector_index])


	def __pb_classificate_click(self):
		try:
			if not self.__func:
				raise AttributeError('Do a train first')

			try:
				point_x = int(self.ui.le_point_x.text())
				point_y = int(self.ui.le_point_y.text())
				point = Point(point_x, point_y)

			except ValueError:
				point = Point(1, 1)

			if self.__func.calc_value(point) >= 0:
				class_number = 0
			else:
				class_number = 1
			self.__training_vectors[class_number].append(point)

			new_coord_x = self.__canvas_width / 2 + point.x * self.__step - self.__point_width / 2
			new_coord_y = self.__canvas_height / 2 - point.y * self.__step - self.__point_height / 2
			self.__draw_point(Point(new_coord_x, new_coord_y), self.__colors[class_number])

			self.ui.le_result.setText(str(class_number))

		except ValueError as ve:
			self.__msgbox_message('Error', str(ve))

		except AttributeError as ae:
			self.__msgbox_message('Error', str(ae))


if __name__ == '__main__':
	potential_controller = PotentialController()
	potential_controller.start()





















