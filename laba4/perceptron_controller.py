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
		self.ui.pb_train.clicked.connect(self.__pb_train_click)

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
			amount_of_classes = int(self.ui.le_amount_of_classes.text())
		except ValueError:
			amount_of_classes = 3

		try:
			amount_of_vectors = int(self.ui.le_amount_of_vectors.text())
		except ValueError:
			amount_of_vectors = 4

		try:
			vector_size = int(self.ui.le_vector_size.text())
		except ValueError:
			vector_size = 6

		training_vectors = self.__generate_training_vectors(amount_of_classes, amount_of_vectors, vector_size)

		perceptron = Perceptron(amount_of_classes, vector_size)
		funcs, isSuccess = perceptron.train(training_vectors)
		if not isSuccess:
			self.__msgbox_message('Error', 'An error occurred while classification')
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

if __name__ == '__main__':
	perceptron_controller = PerceptronController()
	perceptron_controller.start()





















