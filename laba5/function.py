class Function(object):
	def __init__(self, x_coeff, y_coeff, xy_coeff, free_coeff):
		self.__x_coeff = x_coeff
		self.__y_coeff = y_coeff
		self.__xy_coeff = xy_coeff
		self.__free_coeff = free_coeff

	@property
	def x_coeff(self):
		return self.__x_coeff

	@x_coeff.setter
	def x_coeff(self, value):
		self.__x_coeff = value

	@property
	def y_coeff(self):
		return self.__y_coeff

	@y_coeff.setter
	def y_coeff(self, value):
		self.__y_coeff = value

	@property
	def xy_coeff(self):
		return self.__xy_coeff

	@xy_coeff.setter
	def xy_coeff(self, value):
		self.__xy_coeff = value

	@property
	def free_coeff(self):
		return self.__free_coeff

	@free_coeff.setter
	def free_coeff(self, value):
		self.__free_coeff = value
	
	def __str__(self):
		if self.__xy_coeff != 0:
			return 'y = (' + str(-self.__x_coeff) + 'x + ' + \
						str(-self.__free_coeff) + ') / (' + \
						str(self.__xy_coeff) + 'x + ' + \
						str(self.__y_coeff) + ')'
		if self.__y_coeff != 0:
			return 'y = (' + str(-self.__x_coeff / self.__y_coeff) + \
						'x ' + str(-self.__free_coeff / self.__y_coeff)
		if self.__x_coeff != 0:
			return 'x = ' + str(-self.__free_coeff / self.__x_coeff)
		else:
			raise ValueError('x coeffitient is 0')

	def __add__(self, other):
		return Function(self.__x_coeff + other.x_coeff, self.__y_coeff + other.y_coeff, self.__xy_coeff + other.xy_coeff, self.__free_coeff + other.free_coeff)

	def __mul__(self, other):
		return Function(self.__x_coeff * other, self.__y_coeff * other, self.__xy_coeff * other, self.__free_coeff * other)

	def calc_value(self, point):
		return self.__free_coeff + self.__x_coeff * point.x + self.__y_coeff * point.y + self.__xy_coeff * point.x * point.y

	def get_y(self, x):
		return -(self.__x_coeff * x + self.__free_coeff) / (self.__xy_coeff * x + self.__y_coeff)
