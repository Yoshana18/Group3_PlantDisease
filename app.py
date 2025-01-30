from flask import Flask, request, redirect, url_for, render_template
from application import templates
import os

# from pyparsing.diagram import template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html') #render home page


# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         file = request.files['image']
#         if file:
#             filename = os.path.join('static/uploads', file.filename)
#             file.save(filename)
#             # Perform prediction logic here (e.g., call ML model)
#             return redirect(url_for('home'))
#     return render_template('index.html')