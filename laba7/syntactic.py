from PyQt5.QtGui import QPixmap


class SyntacticImage():
	def __init__(self, name, file_path):
		self.__name = name
		self.__file_path = file_path
		self.__pixmap = QPixmap(self.__file_path)

	@property
	def pixmap(self):
		return self.__pixmap
	
	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, value):
		self.__name = value

	@property
	def file_path(self):
		return self.__file_path
	
	@file_path.setter
	def file_path(self, value):
		self.__file_path = value