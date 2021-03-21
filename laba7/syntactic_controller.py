from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os

from syntactic_view import Ui_form_syntactic

from syntactic import SyntacticImage

from point import Point


class ImageScene(QtWidgets.QGraphicsScene):
	click_signal = QtCore.pyqtSignal(float, float)

	def __init__(self):
		super().__init__()

	# overriding mousePressEvent
	def mousePressEvent(self, event):
		cursor_x, cursor_y = event.scenePos().x(), event.scenePos().y()
		self.click_signal.emit(cursor_x, cursor_y)


class SyntacticController(QtCore.QObject):
	def __init__(self):
		super().__init__()
		self.__init_ui_form()
		self.__init_scene()
		self.__init_images()

	def __init_ui_form(self):
		self.app = QtWidgets.QApplication(sys.argv)
		self.form = QtWidgets.QMainWindow()
		self.ui = Ui_form_syntactic()
		self.ui.setupUi(self.form)

	def __init_scene(self):
		self.__canvas_width = 800
		self.__canvas_height = 600
		self.ui.gv_canvas.setFixedSize(self.__canvas_width, self.__canvas_height)

		self.__scene = ImageScene()
		self.__scene.click_signal.connect(self.__click_handler)
		self.__scene.setSceneRect(0, 0, self.__canvas_width, self.__canvas_height)

		self.ui.gv_canvas.setScene(self.__scene)

	def __init_images(self):
		self.__images = []
		base_path = './images'
		search_extension = '.png'
		try:
			for file in [f for f in os.listdir(base_path) if f.endswith(search_extension)]:
				file_name = os.path.splitext(file)[0]
				self.__images.append(SyntacticImage(file_name, '{}/{}'.format(base_path, file)))
		except FileNotFoundError:
			self.__msgbox_message('Error', 'Incorrect path to the images')

	@QtCore.pyqtSlot(float, float)
	def __click_handler(self, x, y):
		current_index = self.ui.cb_primitives.currentIndex()
		if current_index in range(len(self.__images)):
			image = self.__images.pop(current_index)
			pixmap = image.pixmap
			pixmap_item = QtWidgets.QGraphicsPixmapItem(pixmap)

			offset_x = pixmap.width() / 2
			offset_y = pixmap.height() / 2
			pixmap_item.setOffset(-offset_x, -offset_y)
			pixmap_item.setPos(x, y)

			self.__scene.addItem(pixmap_item)

			self.__start_positions[image.name] = Point(x - offset_x, y - offset_y)
			self.__end_positions[image.name] = Point(x - offset_x + offset_x * 2, y - offset_y + offset_y * 2)

			self.ui.cb_primitives.removeItem(current_index)

	def __fill_list_of_primitives(self):
		self.ui.cb_primitives.clear()
		for image in self.__images:
			self.ui.cb_primitives.addItem(image.name)

		if self.__images:
			self.ui.cb_primitives.setCurrentIndex(0)

	def start(self):
		self.__start_positions = {}
		self.__end_positions = {}

		self.ui.pb_clear.clicked.connect(self.__pb_clear_click)
		self.ui.pb_recognize.clicked.connect(self.__pb_recognize_click)

		self.__fill_list_of_primitives()

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

	def __pb_clear_click(self):
		self.ui.gv_canvas.scene().clear()

		self.__start_positions.clear()
		self.__end_positions.clear()

		self.__init_images()
		self.__fill_list_of_primitives()

	def __pb_recognize_click(self):
		pass


if __name__ == '__main__':
	syntactic_controller = SyntacticController()
	syntactic_controller.start()
