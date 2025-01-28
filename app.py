from os import path
import os
from datetime import date
from flask import Flask
from app import app
from flask import render_template

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='app/static')
    app.config.from_object(config_class)

disease_mapping = {
    'Tomato_healthy', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato_Septoria_leaf_spot', 'Tomato_Late_blight',
    'Tomato_Early_blight', 'Tomato_Bacterial_spot', 'Tomato_Leaf_Mold', 'Tomato_Target_Spot',
    'Tomato_Tomato_mosaic_virus', 'Potato_healthy', 'Potato_Late_blight', 'Potato_Early_blight',
    'Grape_Black_rot', 'Grape_healthy', 'Grape_Esca_(Black_Measles)', 'Grape_Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Pepper_bell_Bacterial_spot', 'Pepper_bell_healthy', }
#

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('static/uploads', filename)
        image.save(file_path)
        print(file_path)
        return render_template('index.html')

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)