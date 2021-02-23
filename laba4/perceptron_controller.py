from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from random import randint
import numpy as np

from perceptron_view import Ui_form_perceptron

from perceptron import Perceptron


class PerceptronController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_perceptron()
		self.ui.setupUi(self.form)

	def start(self):
		self.__perceptron = None
		self.__amount_of_classes = 3
		self.__amount_of_vectors = 4
		self.__vector_size = 6

		self.ui.le_amount_of_classes.setPlaceholderText(str(self.__amount_of_classes))
		self.ui.le_amount_of_classes.setText(str(self.__amount_of_classes))

		self.ui.le_amount_of_vectors.setPlaceholderText(str(self.__amount_of_vectors))
		self.ui.le_amount_of_vectors.setText(str(self.__amount_of_vectors))
		
		self.ui.le_vector_size.setPlaceholderText(str(self.__vector_size))
		self.ui.le_vector_size.setText(str(self.__vector_size))

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
			self.__amount_of_classes = int(self.ui.le_amount_of_classes.text())
		except ValueError:
			self.ui.le_amount_of_classes.setText(str(self.__amount_of_classes))

		try:
			self.__amount_of_vectors = int(self.ui.le_amount_of_vectors.text())
		except ValueError:
			self.ui.le_amount_of_vectors.setText(str(self.__amount_of_vectors))

		try:
			self.__vector_size = int(self.ui.le_vector_size.text())
		except ValueError:
			self.ui.le_vector_size.setText(str(self.__vector_size))

		training_vectors = self.__generate_training_vectors(self.__amount_of_classes, self.__amount_of_vectors, self.__vector_size)

		self.__perceptron = Perceptron(self.__amount_of_classes, self.__vector_size)
		funcs, isSuccess = self.__perceptron.train(training_vectors)
		if not isSuccess:
			self.__msgbox_message('Error', 'An error occurred while classification. \nTry again or enter another input data.')
		else:
			self.__fill_result_funcs(funcs)

	def __generate_training_vectors(self, amount_of_classes, amount_of_vectors, vector_size):
		training_vectors = [[np.zeros(vector_size + 1, dtype=int) for i in range(amount_of_vectors)] for j in range(amount_of_classes)]
		return self.__fill_training_vectors(training_vectors)

	def __fill_training_vectors(self, training_vectors):
		added_vectors = []
		for class_vectors in training_vectors:
			for vector in class_vectors:
				vector[-1] = 1
				while True:
					for i in range(len(vector) - 1):
						vector[i] = randint(-50, 50)
					if list(vector) not in added_vectors:
						break
				added_vectors.append(list(vector))
		return training_vectors
	
	def __fill_result_funcs(self, funcs):
		self.ui.pte_functions.clear()
		for func in funcs:
			func_str = ''
			for coeff in func:
				func_str += '| {:^7} |'.format(coeff)
			self.ui.pte_functions.appendPlainText(func_str)
		self.__update_form()

	def __pb_classificate_click(self):
		try:
			if not self.__perceptron:
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
	perceptron_controller = PerceptronController()
	perceptron_controller.start()





















