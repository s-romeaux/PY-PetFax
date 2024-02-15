from flask import ( Blueprint, render_template ) 
import json 

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<int:index>')
def display(index):
    # Make sure the index is within the valid range
    if 0 <= index < len(pets):
        pet = pets[index]
        return render_template('display.html', pet=pet)
    else:
        return "Pet not found", 404