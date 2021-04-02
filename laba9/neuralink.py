import numpy as np

import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist        
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten

from layer_exception import LayerException


class Neuralink():
	def __init__(self, amount_of_inner_layers, activation_functions_for_inner_layers, amount_of_neurons_fo_inner_layers):
		if amount_of_inner_layers != len(activation_functions_for_inner_layers):
			raise LayerException('Incorrect amount of activation functions')

		if amount_of_inner_layers != len(amount_of_neurons_fo_inner_layers):
			raise LayerException('Incorrect length of neurons array')

		self.__amount_of_inner_layers = amount_of_inner_layers
		self.__activation_functions_for_inner_layers = activation_functions_for_inner_layers
		self.__amount_of_neurons_fo_inner_layers = amount_of_neurons_fo_inner_layers

		self.__model = None

	def train(self, batch_size=32, epochs=5, validation_split=0.2):
		(x_train, y_train), (x_test, y_test) = mnist.load_data()
		(x_train, y_train), (x_test, y_test) = self.__normalize(x_train, y_train, x_test, y_test)
		self.__model = self.__create_model()
		self.__model.fit(x_train, y_train_cat, batch_size, epochs, validation_split)
		self.__model.evaluate(x_test, y_test_cat)

	def predict(self):
		pass

	def __normalize(self, x_train, y_train, x_test, y_test):
		x_train /= 255
		x_test /= 255

		y_train_cat = keras.utils.to_categorical(y_train, 10)
		y_test_cat = keras.utils.to_categorical(y_test, 10)

		return (x_train, y_train), (x_test, y_test)

	def __create_model(self):
		model_layers = []

		# input layer
		model_layers.append(Flatten(input_shape=(28, 28, 1)))

		# inner layers
		for layer_num in range(self.__amount_of_inner_layers):
			model_layers.append(Dense(self.__amount_of_neurons_fo_inner_layers[layer_num], activation=self.__activation_functions_for_inner_layers[layer_num]))

		# output layer
		model_layers.append(Dense(10, activation='softmax'))

		model = keras.Sequential(model_layers)
		model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

		return model
