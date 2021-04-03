from PyQt5 import QtCore, QtGui, QtWidgets

import sys

import numpy as np 

from neuralink_view import Ui_form_neuralink

from neuralink import Neuralink
from neuralink_exception import LayerException, ModelError

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
		self.__init_neuralink_image_properties()

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_neuralink()
		self.ui.setupUi(self.form)

	def __init_scene(self):
		self.__canvas_width = 180
		self.__canvas_height = 180
		self.ui.gv_digit.setFixedSize(self.__canvas_width, self.__canvas_height)

		self.__pen_thickness = 6
		self.__scene = DrawScene(self.__pen_thickness)
		self.__scene.setSceneRect(0, 0, self.__canvas_width, self.__canvas_height)

		self.ui.gv_digit.setScene(self.__scene)

	def __init_neuralink_image_properties(self):
		self.__image_width = 28
		self.__image_height = 28
		self.__channels_count = 1
		self.__color_mode = QtGui.QImage.Format_Grayscale8

	def start(self):
		self.ui.pb_train.clicked.connect(self.__pb_train_click)
		self.ui.pb_predict.clicked.connect(self.__pb_predict_click)
		self.ui.pb_clear.clicked.connect(self.__pb_clear_click)

		try:
			self.__neuralink = Neuralink(1, ['relu'], [128])
		except LayerException:
			self.__msgbox_message('Error', str(e))

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
		self.__neuralink.train()

	def __pb_predict_click(self):
		try:
			image_array = self.__get_image_array()
			predicted_res = self.__neuralink.predict(image_array)
			self.ui.le_result.setText(str(np.argmax(predicted_res)))
		except ModelError as e:
			self.__msgbox_message('Error', str(e))


	def __pb_clear_click(self):
		self.__scene.clear()

	def __get_image_array(self):
		image_pixmap = self.ui.gv_digit.grab(self.__scene.sceneRect().toRect())
		
		image = image_pixmap.toImage()
		image = image.scaled(self.__image_width, self.__image_height, transformMode=QtCore.Qt.SmoothTransformation)
		image.convertTo(self.__color_mode)
		image.invertPixels()
		
		image_string = image.bits().asstring(self.__image_width * self.__image_height * self.__channels_count)
		
		image_array = np.frombuffer(image_string, dtype=np.uint8).reshape((self.__image_height, self.__image_width))
		# image_array = image_array % 255
		image_array = image_array / 255

		return image_array

if __name__ == '__main__':
	neuralink_controller = NeuralinkController()
	neuralink_controller.start()
