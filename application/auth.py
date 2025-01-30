from flask import Blueprint, flash, render_template, request, url_for, redirect

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET'])
def home():
    # Main page
    return render_template('index.html') #render home page

