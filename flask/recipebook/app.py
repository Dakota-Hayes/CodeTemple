from flask import Flask, render_template
from dict import recipes

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/recipes/<int:recipe_number>')
def receipe_list(recipe_number):
    return render_template('recipe.html',recipe_id = recipes[recipe_number])

