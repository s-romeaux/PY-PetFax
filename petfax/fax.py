from flask import Blueprint, render_template

fax_bp = Blueprint('fax', __name__, url_prefix="/fax")

@fax_bp.route('/new')
def new():
    return render_template('fax_create.html')
