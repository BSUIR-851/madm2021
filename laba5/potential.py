from function import Function
from point import Point


class Potential(object):
	def __init__(self, amount_of_classes, threshold=50):
		self.__amount_of_classes = amount_of_classes
		self.__threshold = threshold

		self.__result = Function(0, 0, 0, 0)
		self.__correction = 1

	def train(self, training_vectors):
		isContinue = True
		iteration_number = 0
		isSuccess = True
		while isContinue and (iteration_number < self.__threshold):
			iteration_number += 1
			isContinue = self.__iterate(training_vectors)

		if iteration_number >= self.__threshold:
			isSuccess = False
			
		return self.__result, isSuccess

	def __iterate(self, training_vectors):
		isContinue = False

		for vector_index, vector in enumerate(training_vectors):
			for point_index, point in enumerate(vector):
				
				self.__result += self.__get_separating_function(point) * self.__correction
				
				index = (point_index + 1) % len(vector)
				next_class_number = (vector_index + 1) % self.__amount_of_classes if index == 0 else vector_index
				next_point = training_vectors[next_class_number][index]
				
				self.__correction = self.__calc_new_correction(next_point, next_class_number)

				if self.__correction != 0:
					isContinue = True

		return isContinue

	def __get_separating_function(self, point):
		return Function(point.x * 4, point.y * 4, point.x * point.y * 4 * 4, 1)

	def __calc_new_correction(self, next_point, next_class_number):
		function_value = self.__result.calc_value(next_point)
		if (function_value <= 0) and (next_class_number == 0):
			return 1
		if (function_value > 0) and (next_class_number == 1):
			return -1
		return 0


if __name__ == '__main__':

	training_vectors = []
	training_vectors.append([Point(-1, 0), Point(1, 1)])
	training_vectors.append([Point(2, 0), Point(1,-2)])

	amount_of_classes = 2
	potential = Potential(amount_of_classes)

	func, isSuccess = potential.train(training_vectors)
	print(isSuccess)
	print(str(func))

