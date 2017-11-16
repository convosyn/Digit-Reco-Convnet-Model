from keras.models import load_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import skimage.transform as sktrans
import skimage.color as skclr
import json
import skimage
model = load_model('model.h5')
img = sktrans.resize(mpimg.imread('to_predict/' + os.listdir('to_predict/')[0]), (28, 28))
if len(img.shape) > 2:
	img = skclr.rgb2gray(img)
img = img.reshape((1, 1, 28, 28)) 
img *= 255
plt.imshow(img.reshape(28, 28))
plt.show()
pred = model.predict(img).flatten()
print(pred)
ind = (-pred).argsort()[:3].tolist()
pred = pred.tolist()
print(ind)
fpred = {"predictions": []}
for i in ind:
	fpred['predictions'].append({'label': i, 'accuracy': float(pred[i] * 100)})
with open('pred.json', 'w') as fout:
	json.dump(fpred, fout)



