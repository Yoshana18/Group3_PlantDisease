from os import path
import os
from datetime import date
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from app.models import db
from app import init_bp
from flask_migrate import Migrate
from app import app

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='app/static')
    app.config.from_object(config_class)

    db.init_app(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    #
    # with app.app_context():
    #     if not path.exists(app.config['DATABASE_NAME']):
    #         db.create_all()
    #         print('Created Database!')
    # return app

class_mapping = {
    0: 'Tomato_healthy',
    1: 'Tomato_Spider_mites_Two_spotted_spider_mite',
    2: 'Tomato_Septoria_leaf_spot',
    3: 'Tomato_Late_blight',
    4: 'Tomato_Early_blight',
    5: 'Tomato_Bacterial_spot',
    6: 'Tomato_Leaf_Mold',
    7: 'Tomato_Target_Spot',
    8: 'Tomato_Tomato_mosaic_virus',
    9: 'Potato_healthy',
    10: 'Potato_Late_blight',
    11: 'Potato_Early_blight',
    12: 'Grape_Black_rot',
    13: 'Grape_healthy',
    14: 'Grape_Esca_(Black_Measles)',
    15: 'Grape_Leaf_blight_(Isariopsis_Leaf_Spot)',
    16: 'Pepper_bell_Bacterial_spot',
    17: 'Pepper_bell_healthy', }
#
# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         image = request.files['image']
#         filename = image.filename
#         file_path = os.path.join('static/uploads', filename)
#         image.save(file_path)
#         print(file_path)
#         pred = prediction(file_path)
#         title = disease_info['disease_name'][pred]
#         description =disease_info['description'][pred]
#         image_url = disease_info['image_url'][pred]
#         return render_template('submit.html' , title = title , desc = description , image_url = image_url , pred = pred)

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)