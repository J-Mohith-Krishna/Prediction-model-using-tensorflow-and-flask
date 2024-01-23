import numpy as np  
import tensorflow as tf
from flask import Flask, render_template, request
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

model = tf.keras.applications.ResNet50(weights='imagenet')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        file_path = 'image.jpg' 
        file.save(file_path)

        img = image.load_img(file_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.resnet50.preprocess_input(img_array)

        # Make predictions
        preds = model.predict(img_array)
        decoded_preds = decode_predictions(preds, top=3)[0]

        predictions = []
        

  for _, label, score in decoded_preds:
            predictions.append((label, score))

        return render_template('result.html', predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
