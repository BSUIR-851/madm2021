from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import os

from syntactic_view import Ui_form_syntactic

from syntactic import SyntacticImage

from point import Point


class ImageScene(QtWidgets.QGraphicsScene):
	click_signal = QtCore.pyqtSignal(float, float)

	def __init__(self, base_image_path):
		super().__init__()
		self.__base_image_pixmap = QtGui.QPixmap(base_image_path)

	# overriding mousePressEvent
	def mousePressEvent(self, event):
		cursor_x, cursor_y = event.scenePos().x(), event.scenePos().y()
		self.click_signal.emit(cursor_x, cursor_y)

	def drawBackground(self, painter, rect):
		painter.setOpacity(0.1)
		painter.drawPixmap(int(self.width() / 2 - self.__base_image_pixmap.width() / 2), int(self.height() / 2 - self.__base_image_pixmap.height() / 2), self.__base_image_pixmap)

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

		self.__scene = ImageScene('./dog.png')
		self.__scene.click_signal.connect(self.__click_handler)
		self.__scene.setSceneRect(0, 0, self.__canvas_width, self.__canvas_height)

		self.ui.gv_canvas.setScene(self.__scene)

	def __init_images(self):
		self.__images = []
		base_path = './images'
		search_extension = '.png'
		try:
			image_list = os.listdir(base_path)
			image_list.sort()
			for file in [f for f in image_list if f.endswith(search_extension)]:
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
			self.__end_positions[image.name] = Point(x + offset_x, y + offset_y)

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

	def __get_grammar(self):
		grammar = {
			'body': {
				'parent': {
					'name': None,
					'start_x': 50,
					'end_x': 750,
					'start_y': 50,
					'end_y': 550,
				},
				'start_x': self.__start_positions['body'].x,
				'end_x': self.__end_positions['body'].x,
				'start_y': self.__start_positions['body'].y,
				'end_y': self.__end_positions['body'].y,
			},

			'ear': {
				'parent': {
					'name': 'body',
					'start_x': self.__start_positions['body'].x + 115,
					'end_x': self.__start_positions['body'].x + 190,
					'start_y': self.__start_positions['body'].y,
					'end_y': self.__start_positions['body'].y + 129,
				},
				'start_x': self.__start_positions['ear'].x,
				'end_x': self.__end_positions['ear'].x,
				'start_y': self.__start_positions['ear'].y,
				'end_y': self.__end_positions['ear'].y,
			},

			'eye': {
				'parent': {
					'name': 'body',
					'start_x': self.__start_positions['body'].x + 180,
					'end_x': self.__start_positions['body'].x + 207,
					'start_y': self.__start_positions['body'].y + 34,
					'end_y': self.__start_positions['body'].y + 55,
				},
				'start_x': self.__start_positions['eye'].x,
				'end_x': self.__end_positions['eye'].x,
				'start_y': self.__start_positions['eye'].y,
				'end_y': self.__end_positions['eye'].y,
			},

			'front_left_paw': {
				'parent': {
					'name': 'body',
					'start_x': self.__start_positions['body'].x + 175,
					'end_x': self.__start_positions['body'].x + 245,
					'start_y': self.__start_positions['body'].y + 103,
					'end_y': self.__start_positions['body'].y + 170,
				},
				'start_x': self.__start_positions['front_left_paw'].x,
				'end_x': self.__end_positions['front_left_paw'].x,
				'start_y': self.__start_positions['front_left_paw'].y,
				'end_y': self.__end_positions['front_left_paw'].y,
			},

			'hind_left_paw': {
				'parent': {
					'name': 'body',
					'start_x': self.__start_positions['body'].x + 55,
					'end_x': self.__start_positions['body'].x + 95,
					'start_y': self.__start_positions['body'].y + 150,
					'end_y': self.__start_positions['body'].y + 195,
				},
				'start_x': self.__start_positions['hind_left_paw'].x,
				'end_x': self.__end_positions['hind_left_paw'].x,
				'start_y': self.__start_positions['hind_left_paw'].y,
				'end_y': self.__end_positions['hind_left_paw'].y,
			},
		}
		return grammar

	def __analize_grammar_item(self, item):
		isCorrect = False
		if (item.get('start_x') > item.get('parent').get('start_x')) and (item.get('end_x') < item.get('parent').get('end_x')) and (item.get('start_y') > item.get('parent').get('start_y')) and (item.get('end_y') < item.get('parent').get('end_y')):
			isCorrect = True
		return isCorrect

	def __pb_recognize_click(self):
		if self.__images:
			self.__msgbox_message('Recognition error', 'Put all items on canvas')
		else:
			isCorrect = True
			grammar = self.__get_grammar()
			for grammar_item in grammar.keys():
				if not self.__analize_grammar_item(grammar.get(grammar_item)):
					isCorrect = False
					self.__msgbox_message('Recognition error', 'Offset of {} is too big'.format(grammar_item))
					break
			
			if isCorrect:
				self.__msgbox_message('Recognition', 'Object was recognized')
	
if __name__ == '__main__':
	syntactic_controller = SyntacticController()
	syntactic_controller.start()
