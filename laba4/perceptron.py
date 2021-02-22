import numpy as np
from random import randint

from pprint import pprint

class Perceptron(object):
	def __init__(self, amount_of_classes, vector_size, threshold=1000):
		self.__amount_of_classes = amount_of_classes
		self.__vector_size = vector_size
		self.__threshold = threshold

		__polynom_size = self.__vector_size + 1
		self.__funcs = [np.zeros(__polynom_size, dtype=int) for i in range(self.__amount_of_classes)]

	def train(self, training_vectors):
		self.__training_vectors = training_vectors
		isContinue = True
		iteration_number = 1
		isSuccess = True

		while isContinue and (iteration_number < self.__threshold):
			isContinue = self.__iterate()
			iteration_number += 1

		if iteration_number >= self.__threshold:
			isSuccess = False
		return self.__funcs, isSuccess

	def __iterate(self):
		isContinue = False
		for class_number, class_vectors in enumerate(self.__training_vectors):
			for vector in class_vectors:
				if self.__calc(vector, class_number):
					isContinue = True
		return isContinue

	def __calc(self, vector, class_number):
		max_class = self.get_max_function_result(vector)

		if max_class != class_number:
			for func_number, func in enumerate(self.__funcs):
				if func_number == class_number:
					self.__funcs[func_number] = np.add(func, vector, dtype=int)
				else:
					self.__funcs[func_number] = np.subtract(func, vector, dtype=int)
			return True
		return False

	def get_max_function_result(self, vector):
		pretendents = [np.sum(np.dot(func, vector), dtype=int) for func in self.__funcs]
		max_ = max(pretendents)
		max_index = pretendents.index(max_)
		if pretendents.count(max_) != 1:
			max_index = -1
		return max_index


if __name__ == '__main__':
	amount_of_classes = 3
	amount_of_vectors = 4
	vector_size = 6

	training_vectors = [[np.zeros(vector_size + 1, dtype=int) for i in range(amount_of_vectors)] for j in range(amount_of_classes)]
	added_vectors = []
	for class_vectors in training_vectors:
		for vector in class_vectors:
			vector[-1] = 1
			while True:
				for i in range(len(vector) - 1):
					vector[i] = randint(-10, 10)
				if list(vector) not in added_vectors:
					break
			added_vectors.append(list(vector))

	perceptron = Perceptron(amount_of_classes, vector_size)
	funcs, isSuccess = perceptron.train(training_vectors)
	print(isSuccess)
	pprint(funcs)

