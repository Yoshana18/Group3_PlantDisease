from flask import Blueprint, render_template, request
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.preprocessing import image
import numpy as np
# from tensorflow.keras.preprocessing.image import load_img, img_to_array

auth = Blueprint('auth', __name__)

disease_classes = ['Grape - Black Rot', 'Grape - Esca(Black Measles)', 'Grape - Leaf Blight(Isariopsis Leaf Spot)',
                   'Grape - Healthy', 'Pepper Bell - Bacterial Spot', 'Pepper Bell - Healthy', 'Potato - Early Blight',
                   'Potato - Late Blight', 'Potato - Healthy', 'Tomato - Bacterial Spot', 'Tomato - Early Blight',
                   'Tomato - Late Blight', 'Tomato - Leaf Mold', 'Tomato - Septoria leaf spot', 'Tomato - Target Spot',
                   'Tomato - Healthy']

from tensorflow.keras.models import load_model

# check if model is there!
# import os
# model_path = os.path.abspath("my_model.keras")  # Convert to absolute path
# print("Checking model file:", model_path)
# print("File exists:", os.path.exists(model_path))

model_path = r"C:\Users\Yoshana\Documents\GitHub\CV-Project\Plant_Disease\application\my_model.keras"
model = load_model(model_path)

def model_predict(image_path, model):
    img = image.load_img(image_path, color_mode='rgb', target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x /= 255
    custom = model.predict(x)
    return custom

# path = "static/images/Potato/Potato_Early_blight(2).JPG"
# preds = model_predict(path, model)
# a = preds[0]
# ind = np.argmax(a)
# result = disease_classes[ind]
# print(f"the img belongs to:", result)

@auth.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@auth.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part", 400
        f = request.files['file']
        if f.filename == '':
            return "No selected file", 400

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)
        a = preds[0]
        ind = np.argmax(a)
        result = disease_classes[ind]

        return result
    return "Method not allowed", 405
