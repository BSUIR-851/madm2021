from PyQt5 import QtCore, QtGui, QtWidgets, QtChart

import sys

from neuralink_view import Ui_form_neuralink

from point import Point


class DrawScene(QtWidgets.QGraphicsScene):
	def __init__(self, thickness):
		super().__init__()
		self.__is_pressed_left_mouse = False

		self.__pen_thickness = thickness
		self.__pen = QtGui.QPen(QtCore.Qt.black, self.__pen_thickness)
		self.__pen.setCapStyle(QtCore.Qt.RoundCap)
		self.__pen.setJoinStyle(QtCore.Qt.MiterJoin)

		self.__start_point = Point(0, 0)
		self.__end_point = Point(0, 0)

	# override mousePressEvent
	def mousePressEvent(self, event):
		if (event.button() == QtCore.Qt.LeftButton):
			eps = 0.00000001
			self.__is_pressed_left_mouse = True
			self.__start_point.x, self.__start_point.y = event.scenePos().x(), event.scenePos().y()
			self.__end_point.x, self.__end_point.y = self.__start_point.x, self.__start_point.y
			self.addLine(self.__start_point.x, self.__start_point.y, self.__end_point.x + eps, self.__end_point.y + eps, self.__pen)

	# override mouseMoveEvent
	def mouseMoveEvent(self, event):
		if self.__is_pressed_left_mouse:
			self.__end_point.x, self.__end_point.y = event.scenePos().x(), event.scenePos().y()
			self.addLine(self.__start_point.x, self.__start_point.y, self.__end_point.x, self.__end_point.y, self.__pen)
			self.__start_point.x, self.__start_point.y = self.__end_point.x, self.__end_point.y

	# override mouseReleaseEvent
	def mouseReleaseEvent(self, event):
		self.__is_pressed_left_mouse = False


class NeuralinkController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()
		self.__init_scene()

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_neuralink()
		self.ui.setupUi(self.form)

	def __init_scene(self):
		self.__canvas_width = 180
		self.__canvas_height = 180
		self.ui.gv_digit.setFixedSize(self.__canvas_width, self.__canvas_height)

		self.__pen_thickness = 4
		self.__scene = DrawScene(self.__pen_thickness)
		self.__scene.setSceneRect(0, 0, self.__canvas_width, self.__canvas_height)

		self.ui.gv_digit.setScene(self.__scene)

	def start(self):
		self.ui.pb_train.clicked.connect(self.__pb_train_click)
		self.ui.pb_predict.clicked.connect(self.__pb_predict_click)
		self.ui.pb_clear.clicked.connect(self.__pb_clear_click)

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
		pass

	def __pb_predict_click(self):
		pass

	def __pb_clear_click(self):
		self.__scene.clear()

if __name__ == '__main__':
	neuralink_controller = NeuralinkController()
	neuralink_controller.start()
