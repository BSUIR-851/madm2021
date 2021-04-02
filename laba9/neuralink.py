import numpy as np

from keras.datasets import mnist     
from keras.models import Sequential   
from keras.layers import Dense, Flatten
from keras.utils import np_utils
from keras.preprocessing.image import load_img, img_to_array

from neural_exception import LayerException, ModelError


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
		# print(x_test[0])
		(x_train, y_train_cat), (x_test, y_test_cat) = self.__normalize(x_train, y_train, x_test, y_test)
		self.__model = self.__create_model()
		self.__model.fit(x_train, y_train_cat, batch_size, epochs, validation_split)
		self.__model.evaluate(x_test, y_test_cat)

	def predict(self, dataset_to_predict):
		if not self.__model:
			raise ModelError('You have to train before ')
		dataset = np.expand_dims(dataset_to_predict, axis=0)
		predicted_res = self.__model.predict(dataset)
		return predicted_res

	def __normalize(self, x_train, y_train, x_test, y_test):
		x_train = x_train / 255
		x_test = x_test / 255

		y_train_cat = np_utils.to_categorical(y_train, 10)
		y_test_cat = np_utils.to_categorical(y_test, 10)

		return (x_train, y_train_cat), (x_test, y_test_cat)

	def __create_model(self):
		model_layers = []

		# input layer
		model_layers.append(Flatten(input_shape=(28, 28, 1)))

		# inner layers
		for layer_num in range(self.__amount_of_inner_layers):
			model_layers.append(Dense(self.__amount_of_neurons_fo_inner_layers[layer_num], activation=self.__activation_functions_for_inner_layers[layer_num]))

		# output layer
		model_layers.append(Dense(10, activation='softmax'))

		model = Sequential(model_layers)
		model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

		return model


if __name__ == '__main__':
	try:
		neuralink = Neuralink(1, ['relu'], [128])
		neuralink.train()

		image_path = 'hand_2.jpg'
		image = load_img(image_path, color_mode='grayscale', target_size=(28, 28))
		image_arr = img_to_array(image)
		image_arr = image_arr.reshape(28, 28)
		image_arr = image_arr % 255
		image_arr = image_arr / 255
		
		predicted_res = neuralink.predict(image_arr)
		print(predicted_res)
		print(np.argmax(predicted_res))

	except LayerException as e:
		print(e)
	except ModelError as e:
		print(e)
