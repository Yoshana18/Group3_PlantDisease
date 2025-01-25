from os import path
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

    with app.app_context():
        if not path.exists(app.config['DATABASE_NAME']):
            db.create_all()
            print('Created Database!')
    return app


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        file_path = os.path.join('static/uploads', filename)
        image.save(file_path)
        print(file_path)
        pred = prediction(file_path)
        title = disease_info['disease_name'][pred]
        description =disease_info['description'][pred]
        image_url = disease_info['image_url'][pred]
        return render_template('submit.html' , title = title , desc = description , image_url = image_url , pred = pred)

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)