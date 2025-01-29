# disease_mapping = {
#     'Tomato_healthy', 'Tomato_Spider_mites_Two_spotted_spider_mite', 'Tomato_Septoria_leaf_spot', 'Tomato_Late_blight',
#     'Tomato_Early_blight', 'Tomato_Bacterial_spot', 'Tomato_Leaf_Mold', 'Tomato_Target_Spot',
#     'Tomato_Tomato_mosaic_virus', 'Potato_healthy', 'Potato_Late_blight', 'Potato_Early_blight',
#     'Grape_Black_rot', 'Grape_healthy', 'Grape_Esca_(Black_Measles)', 'Grape_Leaf_blight_(Isariopsis_Leaf_Spot)',
#     'Pepper_bell_Bacterial_spot', 'Pepper_bell_healthy', }
# #
#
# @app.route('/predict', methods=['GET', 'POST'])
# def predict():
#     if request.method == 'POST':
#         image = request.files['image']
#         filename = image.filename
#         file_path = os.path.join('static/uploads', filename)
#         image.save(file_path)
#         print(file_path)
#         return render_template('index.html')

# import flask modules
from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html') #render home page

if __name__ == '__main__':
    app.run(port=5000, debug=True)