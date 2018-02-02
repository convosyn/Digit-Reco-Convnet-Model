# Digit Recognition model
It is the base Convnet model used in the [Digit recognition app](https://github.com/convosyn/digit-recognition-app) for android

# How it works

* The images from the server are stored in the `to_predict` folder. Only the first image is used for prediction so make sure that the folder contains only one image at all time which is to be processed. 
* Image is processed by the model
* The results are stored in `predict.json` file. Top-3 predictions are returned as result in a JSON format file. 

## It can be implemented in any app in backend server.
1. Set the image path to `to_predict` folder
2. From inside your program call `predict.py`
3. The results are stored in `pred.json`
4. Pass the results back to your program from the `json` file.
