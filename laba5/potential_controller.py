from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from potential_view import Ui_form_potential

from potential import Potential
from point import Point


class PotentialController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_potential()
		self.ui.setupUi(self.form)

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
			pass
		try:
			self.ui.le_separated_function.setText(str(self.__func))
		except ValueError:
			self.__msgbox_message('Error', 'An error occurred while training. \nEnter another training data.')
	
	def __pb_classificate_click(self):
		try:
			if not self.__func:
				raise AttributeError('Do a train first')

			vector_str = self.ui.le_vector.text().strip()
			vector = [int(num_str) for num_str in vector_str.split(' ')]
			
			if len(vector) != self.__vector_size:
				raise ValueError('Size of vector must be {}'.format(self.__vector_size))

			vector.append(1)
			try:
				max_class = self.__perceptron.get_max_function_result(np.array(vector))
				self.ui.le_result.setText('Class: {}'.format(max_class))
			except ValueError as ve:
				self.__msgbox_message('Error', str(ve))

		except ValueError as ve:
			self.__msgbox_message('Error', str(ve))

		except AttributeError as ae:
			self.__msgbox_message('Error', str(ae))


if __name__ == '__main__':
	potential_controller = PotentialController()
	potential_controller.start()





















