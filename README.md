# Prediction-model-using-tensorflow-and-flask
## EXPLANATION:
### app.py-
    1.	Importing libraries: It imports necessary functions from the Flask framework and Tensorflow API for creating the model and the frontend.
    2.	Initializing model: Here we then initialize the model taken from the ‘tensorflow.keras’ module.
    3.	Routes and Functions: There are in total only 2 main route functions and all the functions will be explained below:
      •	@app.route('/'): This route corresponds to the main page, where users can upload an image for classification. It renders the index.html template.
      •	@app.route('/predict', methods=['POST']): This route is triggered when the user submits the form to predict the image. It loads the uploaded image, makes predictions using a model (loaded from model.h5), and renders the result.html template with the classification results which basically consists of the prediction data of the given image presented through the form.
    4.	Execution: Finally, the script starts the application in debug mode.
    5.	Display: This program will then be displayed in the local host namely <https://127.0.0.1:5000/>.
### index.html and index.css-
    1.	Body: The body basically contains of the Container, a heading and a form for uploading an image for classification using TensorFlow’s Keras model.
    2.	CSS: The CSS here consists of the styling for the index.html page.
### result.html and result.css-
    1.	Body: The body basically contains label for the score and the predictions
    2.	CSS: The CSS here consists of the styling for the result.html page.
