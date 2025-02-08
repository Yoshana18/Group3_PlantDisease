from flask import Blueprint, render_template, request, jsonify
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
import os
from werkzeug.utils import secure_filename

auth = Blueprint('auth', __name__)

# Loading the model here!
model_path = r"C:\Users\Yoshana\Documents\GitHub\CV-Project\Plant_Trial2\application\this_works.keras"
print("File exists:", os.path.exists(model_path))
model = load_model(model_path)
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# for the prediction of the model to run later
def model_predict(image_path, model):
    img = image.load_img(image_path, color_mode='rgb', target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255
    custom = model.predict(x)
    return custom

# The main route for the app
@auth.route('/', methods=['GET'])
def home():
    return render_template('index.html')

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# To handle the image uploads and prediction
@auth.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        print(preds[0])

        disease_classes = ['Grape - Black Rot', 'Grape - Esca(Black Measles)',
                           'Grape - Leaf Blight(Isariopsis Leaf Spot)','Grape - Healthy',
                           'Pepper Bell - Bacterial Spot', 'Pepper Bell - Healthy', 'Potato - Early Blight',
                           'Potato - Late Blight', 'Potato - Healthy', 'Tomato - Bacterial Spot','Tomato - Early Blight',
                           'Tomato - Late Blight', 'Tomato - Leaf Mold', 'Tomato - Septoria leaf spot',
                           'Tomato - Target Spot', 'Tomato - Healthy']

        a = preds[0]
        # ind = np.argmax(a)

        probabilities = preds[0]
        max_index = np.argmax(probabilities)
        max_confidence = probabilities[max_index]

        # Set confidence threshold (adjust as needed)
        CONFIDENCE_THRESHOLD = 0.6

        if max_confidence < CONFIDENCE_THRESHOLD:
            return jsonify({'result': 'Unknown, please try again'})

        result = disease_classes[max_index]
        return jsonify({'result': result, 'confidence': float(max_confidence)})
    return None

