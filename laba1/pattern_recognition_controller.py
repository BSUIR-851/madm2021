from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from pattern_recognition_view import Ui_form_pattern_recognition

from cluster import Cluster
from point import Point

class PatternRecognitionController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.init_ui_form()

	def init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_pattern_recognition()
		self.ui.setupUi(self.form)

	def start(self):
		self.update_form()

		sys.exit(self.app.exec_())

	def update_form(self):
		self.form.hide()
		self.form.show()

	def msgbox_message(self, title, message):
		msgBox = QtWidgets.QMessageBox()
		msgBox.setText(title)
		msgBox.setInformativeText(
			message
		)
		msgBox.exec_()


if __name__ == '__main__':
	pattern_recognition_controller = PatternRecognitionController()
	pattern_recognition_controller.start()