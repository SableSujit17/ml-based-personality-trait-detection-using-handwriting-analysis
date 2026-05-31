from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense
from tensorflow.keras import backend as K

class SmallerVGGNet:
	@staticmethod
	def build(width, height, depth, classes, legacy_names=False):
		
		model = Sequential()
		inputShape = (height, width, depth)
		chanDim = -1

		def layer_name(base_name, index):
			if legacy_names:
				return f"{base_name}_{index}"

			return None

		
		if K.image_data_format() == "channels_first":
			inputShape = (depth, height, width)
			chanDim = 1
		model.add(Conv2D(32, (3, 3), padding="same",
			input_shape=inputShape, name=layer_name("conv2d", 1)))
		model.add(Activation("relu", name=layer_name("activation", 1)))
		model.add(BatchNormalization(axis=chanDim, name=layer_name("batch_normalization", 1)))
		model.add(MaxPooling2D(pool_size=(3, 3), name=layer_name("max_pooling2d", 1)))
		model.add(Dropout(0.25, name=layer_name("dropout", 1)))
		model.add(Conv2D(64, (3, 3), padding="same", name=layer_name("conv2d", 2)))
		model.add(Activation("relu", name=layer_name("activation", 2)))
		model.add(BatchNormalization(axis=chanDim, name=layer_name("batch_normalization", 2)))
		model.add(Conv2D(64, (3, 3), padding="same", name=layer_name("conv2d", 3)))
		model.add(Activation("relu", name=layer_name("activation", 3)))
		model.add(BatchNormalization(axis=chanDim, name=layer_name("batch_normalization", 3)))
		model.add(MaxPooling2D(pool_size=(2, 2), name=layer_name("max_pooling2d", 2)))
		model.add(Dropout(0.25, name=layer_name("dropout", 2)))
		model.add(Conv2D(128, (3, 3), padding="same", name=layer_name("conv2d", 4)))
		model.add(Activation("relu", name=layer_name("activation", 4)))
		model.add(BatchNormalization(axis=chanDim, name=layer_name("batch_normalization", 4)))
		model.add(Conv2D(128, (3, 3), padding="same", name=layer_name("conv2d", 5)))
		model.add(Activation("relu", name=layer_name("activation", 5)))
		model.add(BatchNormalization(axis=chanDim, name=layer_name("batch_normalization", 5)))
		model.add(MaxPooling2D(pool_size=(2, 2), name=layer_name("max_pooling2d", 3)))
		model.add(Dropout(0.25, name=layer_name("dropout", 3)))
		model.add(Flatten(name=layer_name("flatten", 1)))
		model.add(Dense(1024, name=layer_name("dense", 1)))
		model.add(Activation("relu", name=layer_name("activation", 6)))
		model.add(BatchNormalization(name=layer_name("batch_normalization", 6)))
		model.add(Dropout(0.5, name=layer_name("dropout", 4)))
		model.add(Dense(classes, name=layer_name("dense", 2)))
		model.add(Activation("softmax", name=layer_name("activation", 7)))

		return model
