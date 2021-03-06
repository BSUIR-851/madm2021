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

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_potential()
		self.ui.setupUi(self.form)

	def __init_scene(self):
		self.pen_width = 1
		self.canvas_width = self.ui.gv_graphic.size().width() - 10
		self.canvas_height = self.ui.gv_graphic.size().height() - 10

		self.scene = QtWidgets.QGraphicsScene()
		self.scene.setSceneRect(0, 0, self.canvas_width, self.canvas_height)
		self.ui.gv_graphic.setScene(self.scene)

	def start(self):
		self.__func = None
		self.__amount_of_classes = 2

		self.__training_vectors = []
		self.__training_vectors.append([Point(-1, 0), Point(1, 1)])
		self.__training_vectors.append([Point(2, 0), Point(1,-2)])

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
			pass

		try:
			class_1_point_0_x = int(self.ui.le_class_1_point_0_x.text())
			class_1_point_0_y = int(self.ui.le_class_1_point_0_y.text())
			point_0 = Point(class_1_point_0_x, class_1_point_0_y)

			class_1_point_1_x = int(self.ui.le_class_1_point_1_x.text())
			class_1_point_1_y = int(self.ui.le_class_1_point_1_y.text())
			point_1 = Point(class_1_point_1_x, class_1_point_1_y)

			self.__training_vectors[1] = [point_0, point_1]
		except ValueError:
			pass

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
		pen.setWidth(self.pen_width)
		brush = QtGui.QBrush(color)
		self.scene.addElipse(point.x, point.y, self.point_size[0], self.point_size[1], pen, brush)

	def __draw_line(self, start_point, end_point, color):
		pen = QtGui.QPen(color)
		pen.setWidth(self.pen_width)
		self.scene.addLine(start_point.x, start_point.y, end_point.x, end_point.y, pen)

	def __draw_axes(self):
		start_point = Point(0, self.canvas_height / 2)
		end_point = Point(self.canvas_width, self.canvas_height / 2)
		self.__draw_line(start_point, end_point, QtGui.QColor('black'))

		start_point = Point(self.canvas_width / 2, 0)
		end_point = Point(self.canvas_width/ 2, self.canvas_height)
		self.__draw_line(start_point, end_point, QtGui.QColor('black'))

	def __draw_graphic(self):
		pass

	def __draw_training_points(self):
		pass

	def __pb_classificate_click(self):
		try:
			if not self.__func:
				raise AttributeError('Do a train first')

			pass

		except ValueError as ve:
			self.__msgbox_message('Error', str(ve))

		except AttributeError as ae:
			self.__msgbox_message('Error', str(ae))


if __name__ == '__main__':
	potential_controller = PotentialController()
	potential_controller.start()





















