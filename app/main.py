from flask import Blueprint, render_template

main = Blueprint('Main', __name__)

@main.route('/')
def home():
    return render_template("index.html")