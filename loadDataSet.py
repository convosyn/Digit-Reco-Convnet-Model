import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as imgplt
from keras import backend as K
K.set_image_dim_ordering('th')
def ld():
	file_train, file_test = 'train.csv', 'test.csv'
	train, test = np.array(pd.read_csv(file_train), dtype='float64'), np.array(pd.read_csv(file_test), dtype='float64')
	sp_train = train.shape[0]
	sp_test = test.shape[0]
	Xtrain, Ytrain, Xtest = train[:, 1:], train[:, 0], test
	Xtrain, Xtest = Xtrain.reshape(sp_train, 1, 28, 28), Xtest.reshape(sp_test, 1, 28, 28)
	print("testing data set image: ")
	img1 = Xtrain[0].reshape(28, 28)
	img2 = Xtest[0].reshape(28, 28)
	plt.subplot(2, 1, 1)
	plt.imshow(img1)
	plt.subplot(2, 1, 2)
	plt.imshow(img2)
	plt.show()
	return Xtrain, Ytrain, Xtest