from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

import sys
from random import randint

from hierarchy_view import Ui_form_hierarchy

from hierarchy import Hierarchy


class HierarchyController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()
		self.__init_chart()

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_hierarchy()
		self.ui.setupUi(self.form)

	def __init_chart(self):
		self.__chart = QtChart.QChart()
		self.__chart_view = QtChart.QChartView(self.__chart)
		self.ui.vl_chart_view.addWidget(self.__chart_view)

	def __remove_chart_from_layout(self):
		self.ui.vl_chart_view.removeWidget(self.__chart_view)

	def start(self):
		self.__amount_of_objects = 2
		
		self.ui.cb_classification_criterion.addItems(['Minimum', 'Maximum'])
		self.ui.cb_classification_criterion.setCurrentIndex(0)

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

	def __pb_classificate_click(self):
		self.__remove_chart_from_layout()
		self.__init_chart()
		try:
			self.__amount_of_objects = int(self.ui.le_amount_of_objects.text())

		except ValueError:
			pass
		# self.__distances = [[0.0, 6.0, 5.0], [6.0, 0.0, 2.0], [5.0, 2.0, 0.0]]
		self.__distances = self.__generate_random_distances(self.__amount_of_objects)
		print(self.__distances)
		hierarchy = Hierarchy(self.__distances, self.__amount_of_objects)
		hierarchy.find_groups()
		hierarchy.draw(self.__chart)
		self.__chart.createDefaultAxes()
		self.__update_form()

	def __generate_random_distances(self, size):
		distances = []
		for i in range(size):
			temp_distances = []
			for j in range(size):
				temp_distances.append(0)
			distances.append(temp_distances)

		for i in range(1, size):
			for j in range(0, i):
				distances[i][j] = randint(0, size + 5)
				distances[j][i] = distances[i][j]

		if self.ui.cb_classification_criterion.currentIndex() == 1:
			for i in range(1, size):
				for j in range(0, i):
					distances[i][j] = size + 5 - distances[i][j]
					distances[j][i] = distances[i][j]
		return distances


if __name__ == '__main__':
	hierarchy_controller = HierarchyController()
	hierarchy_controller.start()
